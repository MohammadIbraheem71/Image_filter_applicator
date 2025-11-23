import express from "express";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import db from "../database.js";

const router = express.Router();

//this is the sign up path
router.post("/signup", async(req, res) => {
    const {username, email, password} = req.body;

    if (!email || !username || !password) {
        return res.status(400).json({ error: "email, username, and password are required" });
    }

    try{
        const hash = await bcrypt.hash(password, 10);
        const statement = db.prepare("INSERT INTO users (email, username,  password_hash) VALUES (?, ?, ?)");
        statement.run(email, username, hash);
        res.status(201).json({message: "user sucessfully registered."});
    }
    catch (err){
        console.log(err)
        res.status(400).json({error: "email or username already registered."});
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

    const match = await bcrypt.compare(password, user.password_hash)
    if (!match){
        return res.status(400).json({error: "invalid password or email."});
    }

    const token = jwt.sign({id: user.id, email:user.email, username: user.username}, process.env.JWT_SECRET);
    res.json({token});
});



export default router;
