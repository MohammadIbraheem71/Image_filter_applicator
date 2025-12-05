import express from "express";
import multer from "multer";
import fs from "fs";
import {v2 as cloudinary} from "cloudinary";
import jwt from "jsonwebtoken";
import db from "../database.js";

// import dotenv from "dotenv";
// dotenv.config()

//upload.js file
//image uploading stuff here

const router = express.Router();
const upload = multer({dest: "uploads/"});

cloudinary.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET,
});

console.log("cloudinary config information:", {
  name: process.env.CLOUDINARY_CLOUD_NAME,
  key: process.env.CLOUDINARY_API_KEY ? "loaded" : "missing",
  secret: process.env.CLOUDINARY_API_SECRET ? "loaded" : "missing",
});


//this verifies the users token to ensure that the user is logged in
function authentication_middleware(req, res, next){
    const header = req.headers.authorization;
    if (!header){
        console.log("authentication failed, no token provided")
        return res.status(401).json({error: "no token provided."});
    }

    try{
        const token = header.split(" ")[1];
        req.user = jwt.verify(token, process.env.JWT_SECRET);
        console.log(`authentication sucessful for user ID: ${req.user.id}`)
        next();
    }
    catch{
        res.status(403).json({ error: "invalid token."});
    }
}


//upload an image here
router.post("/upload", authentication_middleware, upload.single("image"), async(req, res)=>{
    try{
        const result = await cloudinary.uploader.upload(req.file.path);
        console.log(`Image uploaded to Cloudinary: ${result.secure_url}`);
        fs.unlinkSync(req.file.path);

        const statement = db.prepare("INSERT INTO images (user_id, filename, image_url) VALUES (?, ?, ?)")
        statement.run(req.user.id, req.body.filename, result.secure_url)
        console.log(`image saved to database with filename: ${req.body.filename}`);
        res.status(201).json({ message: "image uploaded sucessfully.", url:result.secure_url});
    }
    catch(err){
        console.log("upload error:", err.message)
        res.status(500).json({ error: err.message});
    }
});

// Get ONLY the logged-in user's gallery (same format as /gallery)
router.get("/user_gallery", authentication_middleware, (req, res) => {
  try {
    const userId = req.user.id;

    // Fetch user's images
    const images = db
      .prepare("SELECT * FROM images WHERE user_id = ?")
      .all(userId);

    console.log(`Found ${images.length} images for user ID: ${userId}`);
    // Compute likes + liked_by_user (always true since these are user's own images)
    const imagesWithLikes = images.map((img) => {
      const likesRow = db
        .prepare("SELECT COUNT(*) AS likes FROM image_likes WHERE image_id = ?")
        .get(img.id);

      const likedRow = db
        .prepare("SELECT 1 FROM image_likes WHERE image_id = ? AND user_id = ?")
        .get(img.id, userId);

      return {
        ...img,
        likes: likesRow.likes,
        liked_by_user: !!likedRow, // true if user has liked their own image
      };
    });

    console.log(`User gallery fetched successfully for user ID: ${userId}`);

    return res.status(200).json({
      success: true,
      count: imagesWithLikes.length,
      images: imagesWithLikes,
    });

  } catch (error) {
    console.error("Error fetching user gallery:", error);
    return res.status(500).json({
      success: false,
      message: "Failed to load user gallery",
    });
  }
});


//delete an image
router.delete("/delete/:id", authentication_middleware, async (req, res) => {
  console.log(`delete requset for imageID: ${req.params.id} by user: ${req.user.id}`)
  const image = db.prepare("SELECT * FROM images WHERE id = ? AND user_id = ?").get(req.params.id, req.user.id);
  if (!image){
    console.log(`image not found or unauthouirzed`)
    return res.status(404).json({ error: "Image not found" });
  } 

  try {
    // Extract Cloudinary public ID (the part after last '/')
    const publicId = image.image_url.split("/").pop().split(".")[0];
    await cloudinary.uploader.destroy(publicId);
    console.log(`image deleted from cloudinary: ${publicId}`)

    db.prepare("DELETE FROM images WHERE id = ?").run(req.params.id);
    console.log(`image deleted from database: image id = ${req.params.id}`)
    res.status(200).json({ message: "Deleted successfully" });
  } catch (err) {
    console.log(`error deleting image: ${req.params.id}, err.message`)
    res.status(500).json({ error: err.message });
  }
});

//this function gets and returns the shared gallery, we dont need to authenticate for that
//gets the shared gallery
router.get("/gallery", async (req, res) => {
  try {
    // Check if user is logged in
    let userId = null;
    const header = req.headers.authorization;
    if (header) {
      try {
        const token = header.split(" ")[1];
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        userId = decoded.id;
        console.log(`Authenticated user viewing gallery: User ID ${userId}`);
      } catch (err) {
        // Invalid token, treat as guest
        console.log("Invalid token in gallery request, treating as guest");
        userId = null;
      }
    }
    else{
      console.log("guest user viewing gallery")
    }

    // Get all images
    const images = db.prepare("SELECT * FROM images").all();
    console.log(`Total images in gallery: ${images.length}`);

    // Add likes and liked_by_user
    const imagesWithLikes = images.map((img) => {
      const likesRow = db
        .prepare("SELECT COUNT(*) AS likes FROM image_likes WHERE image_id = ?")
        .get(img.id);

      let likedByUser = false;
      if (userId) {
        const likedRow = db
          .prepare("SELECT 1 FROM image_likes WHERE image_id = ? AND user_id = ?")
          .get(img.id, userId);
        likedByUser = !!likedRow;
      }

      return {
        ...img,
        likes: likesRow.likes,
        liked_by_user: likedByUser,
      };
    });

    console.log("Gallery fetched successfully");
    return res.status(200).json({
      success: true,
      count: imagesWithLikes.length,
      images: imagesWithLikes,
    });
  } catch (error) {
    console.error("Error fetching gallery:", error);
    return res.status(500).json({
      success: false,
      message: "Failed to load gallery",
    });
  }
});


//this function searches for a singular image by its image id
//we dont use authentication middleware here because here authentication is optional
//not compulsory
router.get("/get_single_img/:id", async (req, res) => {
  console.log(`Single image request: Image ID ${req.params.id}`);
  try {
    const imageId = req.params.id;

    // --- Check logged-in status (optional) ---
    let userId = null;
    const header = req.headers.authorization;
    if (header) {
      try {
        const token = header.split(" ")[1];
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        userId = decoded.id;
        console.log(`Authenticated user viewing image: User ID ${userId}`);
      } catch {
        console.log("Invalid token in single image request, treating as guest");
        userId = null; // guest
      }
    }
    else {
      console.log("👤 Guest user viewing single image");
    }

    // --- Fetch image from DB ---
    const image = db.prepare("SELECT * FROM images WHERE id = ?").get(imageId);

    if (!image) {
      console.log(`Image not found: Image ID ${imageId}`);
      return res.status(404).json({ 
        success: false, 
        message: "Image not found" 
      });
    }

    // --- Count likes ---
    const likesData = db
      .prepare("SELECT COUNT(*) AS likes FROM image_likes WHERE image_id = ?")
      .get(imageId);

    // --- Determine if user liked it ---
    let likedByUser = false;
    if (userId) {
      const likedRow = db
        .prepare("SELECT 1 FROM image_likes WHERE image_id = ? AND user_id = ?")
        .get(imageId, userId);
      likedByUser = !!likedRow;
    }

    // --- OPTIONAL: Get uploader info ---
    const uploader = db
      .prepare("SELECT username FROM users WHERE id = ?")
      .get(image.user_id);

    console.log(`Single image fetched successfully: Image ID ${imageId}, Likes: ${likesData.likes}`);
    return res.status(200).json({
      success: true,
      image: {
        ...image,
        likes: likesData.likes,
        liked_by_user: likedByUser,
        uploader: uploader ? uploader.username : null,
      },
    });
  } catch (error) {
    console.error(`Error fetching image ID ${req.params.id}:`, error.message);
    return res.status(500).json({
      success: false,
      message: "Failed to fetch image",
    });
  }
});


//like route
router.post("/like", authentication_middleware, (req, res) => {
    const userId = req.user.id;
    const { image_id } = req.body;

    console.log(`Like request: User ID ${userId}, Image ID ${image_id}`);

    if (!image_id) {
        console.log("Like failed: Missing image_id");
        return res.status(400).json({ success: false, message: "Missing image_id" });
    }

    try {
        const stmt = db.prepare(`
            INSERT INTO image_likes (user_id, image_id) 
            VALUES (?, ?)
        `);
        stmt.run(userId, image_id);
        
        console.log(`Image liked successfully: User ID ${userId}, Image ID ${image_id}`);

        return res.json({ success: true, message: "Liked" });
    } catch (err) {
        if (err.message.includes("UNIQUE")) {
            console.log(`Like failed: User ID ${userId} already liked Image ID ${image_id}`);
            return res.status(400).json({ success: false, message: "Already liked" });
        }
        console.error(`Like error: User ID ${userId}, Image ID ${image_id}:`, err.message);
        return res.status(500).json({ success: false, message: "Server error" });
    }
});

//unlike route
router.post("/unlike", authentication_middleware, (req, res) => {
    const userId = req.user.id;
    const { image_id } = req.body;

     console.log(`Unlike request: User ID ${userId}, Image ID ${image_id}`);

    if (!image_id) {
        console.log("Unlike failed: Missing image_id");
        return res.status(400).json({ success: false, message: "Missing image_id" });
    }
    try {
        const stmt = db.prepare(`
            DELETE FROM image_likes 
            WHERE user_id = ? AND image_id = ?
        `);
        const result = stmt.run(userId, image_id);
        
        if (result.changes === 0) {
            console.log(`Unlike failed: No like found for User ID ${userId}, Image ID ${image_id}`);
        } else {
            console.log(`Image unliked successfully: User ID ${userId}, Image ID ${image_id}`);
        }

        return res.json({ success: true, message: "Unliked" });
    } catch (err) {
        console.error(`Unlike error: User ID ${userId}, Image ID ${image_id}:`, err.message);
        return res.status(500).json({ success: false, message: "Server error" });
    }
});



export default router;