import express from "express";
import multer from "multer";
import fs from "fs";
import {v2 as cloudinary} from "cloudinary";
import jwt from "jsonwebtoken";
import db from "../database.js";


//upload.js file
//image uploading stuff here

const router = express.Router();
const upload = multer({dest: "uploads/"});

cloudinary.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET,
});

//this verifies the users token to ensure that the user is logged in
function authentication_middleware(req, res, next){
    const header = req.headers.authourization;
    if (!header){
        return res.status(401).json({error: "no token provided."});
    }

    try{
        const token = header.split(" ")[1];
        req.user = jwt.verify(token, process.env.JWT_SECRET);
    }
    catch{
        res.status(403).json({ error: "invalid token."});
    }
}

router.post("/", authentication_middleware, upload.single("image"), async(req, res)=>{
    try{
        const result = await cloudinary.uploader.upload(req.file.path);
        fs.unlinkSync(req.file.path);

        const statement = db.prepare("INSERT INTO images (user_id, filename, image_url) VALUES (?, ?, ?)")
        statement.run(req.user.id, req.file.originalname, result.secure_url)
        res.json({ message: "image uploaded sucessfully.", url:result.secure_url});
    }
    catch(err){
        res.status(500).json({ error: err.message});
    }
});