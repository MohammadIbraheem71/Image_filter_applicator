
import "dotenv/config";

//dotenv.config()

console.log("Environment variables check:", {
  cloudName: process.env.CLOUDINARY_CLOUD_NAME ? "loaded" : "missing",
  apiKey: process.env.CLOUDINARY_API_KEY ? "loaded" : "missing",
  apiSecret: process.env.CLOUDINARY_API_SECRET ? "loaded" : "missing",
  jwtSecret: process.env.JWT_SECRET ? "loaded" : "missing",
  pass: process.env.PASS ? "loaded" : "missing",
  email: process.env.EMAIL ? "loaded" : "missing"
});

import express from "express";
import cors from "cors";
import authRouter from "./routes/auth.js";
import imageRouter from "./routes/image.js";


const app = express();

app.use(cors());
app.use(express.json());

app.use("/routes/auth", authRouter);
app.use("/routes/image", imageRouter);

app.listen(3000, ()=>{
    console.log("server listening on port 3000");
});