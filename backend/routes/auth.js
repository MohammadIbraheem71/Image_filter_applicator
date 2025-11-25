import express from "express";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import nodemailer from "nodemailer"
import db from "../database.js";

const router = express.Router();

const transporter = nodemailer.createTransport({
    secure: true,
    host: "smtp.gmail.com",
    port: 465,
    auth: {
        user: "sara.rehman700@gmail.com", // your Gmail account
        pass: "" // Gmail App password (no spaces)
    }
});
//Function for sending mail using transporter
async function sendVerificationEmail(to, token) {
    const url = `http://localhost:3000/routes/auth/verify-email?token=${token}`;
    await transporter.sendMail({
        from: `"Image Filter Application" <sara.rehman700@gmail.com>`,
        to,
        subject: "Verify your email",
        html: `<p>Click <a href="${url}">here</a> to verify your email.</p>`
    });
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
    res.json({token});
});



export default router;
