import Database from "better-sqlite3";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const db_path = path.join(__dirname, "photoEz.db");


const db = new Database(db_path, {verbose: console.log});


//here we check if the db connection works or not
try{
    db.prepare("SELECT 1").get();
    console.log("connected to the sqlite database");
}catch (err){
    console.log("failed to connect to sqlite database error: ", err.message);
    process.exit(1);
}

export default db;