import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import authRouter from "./routes/auth.js";
import uploadRouter from "./routes/upload.js";

dotenv.config()
const app = express();

