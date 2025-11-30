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
        return res.status(401).json({error: "no token provided."});
    }

    try{
        const token = header.split(" ")[1];
        req.user = jwt.verify(token, process.env.JWT_SECRET);
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
        fs.unlinkSync(req.file.path);

        const statement = db.prepare("INSERT INTO images (user_id, filename, image_url) VALUES (?, ?, ?)")
        statement.run(req.user.id, req.body.filename, result.secure_url)
        res.status(201).json({ message: "image uploaded sucessfully.", url:result.secure_url});
    }
    catch(err){
        res.status(500).json({ error: err.message});
    }
});

//gets the users images
router.get("/", authentication_middleware, (req, res) => {
    const rows = db.prepare("SELECT * FROM images WHERE user_id = ?").all(req.user.id);
    res.json(rows);
});

//delete an image
router.delete("/:id", authentication_middleware, async (req, res) => {
  const image = db.prepare("SELECT * FROM images WHERE id = ? AND user_id = ?").get(req.params.id, req.user.id);
  if (!image) return res.status(404).json({ error: "Image not found" });

  try {
    // Extract Cloudinary public ID (the part after last '/')
    const publicId = image.image_url.split("/").pop().split(".")[0];
    await cloudinary.uploader.destroy(publicId);

    db.prepare("DELETE FROM images WHERE id = ?").run(req.params.id);
    res.status(200).json({ message: "Deleted successfully" });
  } catch (err) {
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
      } catch (err) {
        // Invalid token, treat as guest
        userId = null;
      }
    }

    // Get all images
    const images = db.prepare("SELECT * FROM images").all();

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


//like route
router.post("/like", authentication_middleware, (req, res) => {
    const userId = req.user.id;
    const { image_id } = req.body;

    if (!image_id) return res.status(400).json({ success: false, message: "Missing image_id" });

    try {
        const stmt = db.prepare(`
            INSERT INTO image_likes (user_id, image_id) 
            VALUES (?, ?)
        `);
        stmt.run(userId, image_id);

        return res.json({ success: true, message: "Liked" });
    } catch (err) {
        if (err.message.includes("UNIQUE")) {
            return res.status(400).json({ success: false, message: "Already liked" });
        }
        console.error("Like error:", err);
        return res.status(500).json({ success: false, message: "Server error" });
    }
});

//unlike route
router.post("/unlike", authentication_middleware, (req, res) => {
    const userId = req.user.id;
    const { image_id } = req.body;

    if (!image_id) return res.status(400).json({ success: false, message: "Missing image_id" });

    try {
        const stmt = db.prepare(`
            DELETE FROM image_likes 
            WHERE user_id = ? AND image_id = ?
        `);
        stmt.run(userId, image_id);

        return res.json({ success: true, message: "Unliked" });
    } catch (err) {
        console.error("Unlike error:", err);
        return res.status(500).json({ success: false, message: "Server error" });
    }
});



export default router;