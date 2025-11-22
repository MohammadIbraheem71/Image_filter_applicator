import express from "express";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import db from "../database.js";

const router = express.Router();

//this is the sign up path
router.post("/signup", async(req, res) => {
    const {email, password} = req.body;
    try{
        const hash = await bcrypt.hash(password, 10);
        const statement = db.prepare("INSERT INTO users (email, password_hash) VALUES (?, ?)");
        statement.run(email, hash);
        res.status(201).json({message: "user sucessfully registered."});
    }
    catch (err){
        res.status(400).json({error: "email already registered."});
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

    const token = jwt.sign({id: user.id, email:user.email}, process.env.JWT_SECRET);
    res.json({token});
});



export default router;
