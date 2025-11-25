import Database from "better-sqlite3";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// path to your database
const db_path = path.join(__dirname, "photoEz.db");
const db = new Database(db_path);

console.log("Creating tables if they don't exist...");

// Use IF NOT EXISTS so running multiple times is safe
db.exec(`
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  is_verified INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS images (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  filename TEXT NOT NULL,
  image_url TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
`);

console.log("Tables created successfully!");
db.close();
