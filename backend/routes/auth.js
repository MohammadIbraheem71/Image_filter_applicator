import express from "express";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import nodemailer from "nodemailer"
import db from "../database.js";

const router = express.Router();

console.log("email information:", {
  email: process.env.EMAIL ? "loaded" : "missing",
  password: process.env.PASS ? "loaded" : "missing"
});

import crypto from "crypto";
function generateShortToken(length = 6) {
  //Alphanumeric uppercase only for simplicity
  return crypto.randomBytes(length).toString("hex").slice(0, length).toUpperCase();
}

const transporter = nodemailer.createTransport({
    secure: true,
    host: "smtp.gmail.com",
    port: 465,
    auth: {
        user: process.env.EMAIL, // your Gmail account
        pass: process.env.PASS // Gmail App password (no spaces)
    }
});
//the function for sending mail using transporter through nodemailer
async function sendVerificationEmail(to, token) {
    const url = `http://localhost:3000/routes/auth/verify-email?token=${token}`;
    await transporter.sendMail({
        from: `"Image Filter Application" <${process.env.EMAIL}>`,
        to,
        subject: "Verify your email",
        html: `<p>Click <a href="${url}">here</a> to verify your email.</p>`
    });
}

//Function for sending resetPassword mail
async function sendPasswordResetEmail(to, token) {
    // Plain token 
    await transporter.sendMail({
        from: `"Image Filter Application" <${process.env.EMAIL}>`,
        to,
        subject: "Reset your password",
        html: `
            <p>You requested a password reset.</p>
            <p>Your reset token is:</p>
            <h2>${token}</h2>
            <p>Open your application and enter this token along with your new password.</p>
        `
    });
}

function isValidEmail(email) {
    // Basic regex for standard email format
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}


//this is the sign up path
router.post("/signup", async (req, res) => {
    const { username, email, password } = req.body;

    if (!email || !username || !password) {
        return res.status(400).json({ error: "Email, username, and password are required" });
    }

    try {
        const existing = db.prepare("SELECT * FROM users WHERE email = ? OR username = ?").get(email, username);
        if (existing) return res.status(400).json({ error: "Email or username already registered" });

         if (!isValidEmail(email)) {
            return res.status(400).json({ error: "Invalid email format" });
        }

        const hash = await bcrypt.hash(password, 10);

        // Insert user with is_verified = 0
        db.prepare("INSERT INTO users (email, username, password_hash, is_verified) VALUES (?, ?, ?, 0)")
          .run(email, username, hash);

        // Generate JWT token for verification
        const token = jwt.sign({ email }, process.env.JWT_SECRET, { expiresIn: "1h" });

        await sendVerificationEmail(email, token);

        res.status(201).json({ message: "User registered. Please check your email to verify your account." });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: "Server error" });
    }
});

//verification route
router.get("/verify-email", (req, res) => {
    const { token } = req.query;
    try {
        const payload = jwt.verify(token, process.env.JWT_SECRET);
        db.prepare("UPDATE users SET is_verified = 1 WHERE email = ?").run(payload.email);
        res.send("Email verified! You can now log in.");
    } catch (err) {
        res.status(400).send("Invalid or expired token.");
    }
});


//this is the login path
router.post("/login", async (req, res) =>{
    const {email, password} = req.body;
    const statement = db.prepare("SELECT * FROM users WHERE email = ?");
    const user = statement.get(email);

    if (!user){
        return res.status(400).json({error: "user not registered."});
    }

    if (!user.is_verified) {
        return res.status(403).json({ error: "Please verify your email before logging in." });
    }

    const match = await bcrypt.compare(password, user.password_hash)
    if (!match){
        return res.status(400).json({error: "invalid password or email."});
    }

    const token = jwt.sign({id: user.id, email:user.email, username: user.username}, process.env.JWT_SECRET);
    res.json({token, 
        user: {
            id: user.id,
            username: user.username,
            is_verified: user.is_verified
        }});
    });


// Temporary in-memory store for one-time tokens
const resetTokens = new Map(); // userId -> token

//route for resetting passwrod (resetreq dialog)
router.post("/reset-password-request", (req, res) => {
  const { email } = req.body;
  const user = db.prepare("SELECT * FROM users WHERE email = ?").get(email);
  if (!user) return res.status(404).json({ error: "User not found" });

  const token = generateShortToken(6);

  // store token in temprary memory
  resetTokens.set(user.id, token);

  // send the token via email (nodemailer)
  sendPasswordResetEmail(user.email, token);

  res.json({ message: "Reset token sent via email" });
});

//route for reseting passwrd (resetpass dialog)
router.post("/reset-password", async (req, res) => {
  const { token, newPassword } = req.body;

  if (!token || !newPassword)
    return res.status(400).json({ error: "Token and new password required" });

  // Find userId by token
  let userId = null;
  for (const [id, t] of resetTokens.entries()) {
    if (t === token) {
      userId = id;
      break;
    }
  }

  if (!userId) return res.status(400).json({ error: "Invalid or expired token" });

  const user = db.prepare("SELECT * FROM users WHERE id = ?").get(userId);
  if (!user) return res.status(404).json({ error: "User not found" });

  // new password to be hashed
  const hash = await bcrypt.hash(newPassword, 10);
  db.prepare("UPDATE users SET password_hash = ? WHERE id = ?").run(hash, user.id);

  // Remove token (one-time use)
  resetTokens.delete(user.id);

  res.json({ message: "Password reset successfully!" });
});


export default router;
