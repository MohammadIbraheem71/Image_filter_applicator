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
C-- -------------------------
-- Users table
-- -------------------------
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    is_verified INTEGER DEFAULT 0
);

-- -------------------------
-- Images table
-- -------------------------
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    filename TEXT NOT NULL,
    image_url TEXT NOT NULL,
    likes INTEGER DEFAULT 0,
    uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- -------------------------
-- Junction table for likes
-- -------------------------
CREATE TABLE IF NOT EXISTS image_likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    image_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, image_id),  -- prevents double-likes
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (image_id) REFERENCES images(id)
);

-- -------------------------
-- Trigger: Increment likes after like
-- -------------------------
CREATE TRIGGER IF NOT EXISTS trigger_increment_likes
AFTER INSERT ON image_likes
BEGIN
    UPDATE images
    SET likes = likes + 1
    WHERE id = NEW.image_id;
END;

-- -------------------------
-- Trigger: Decrement likes after unlike
-- -------------------------
CREATE TRIGGER IF NOT EXISTS trigger_decrement_likes
AFTER DELETE ON image_likes
BEGIN
    UPDATE images
    SET likes = likes - 1
    WHERE id = OLD.image_id;
END;

`);

console.log("Tables created successfully!");
db.close();
