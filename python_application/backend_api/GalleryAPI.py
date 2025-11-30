import requests
import mimetypes
import os
from PySide6.QtCore import QObject, Signal

class GalleryAPI(QObject):
    image_uploaded = Signal()
    image_liked = Signal()   # new signal
    image_unliked = Signal() 

    def __init__(self, base_url, token=None, http_client=requests):
        super().__init__()
        self.base_url = base_url
        self.token = token
        self.http_client = http_client

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    #function to get gallery
    def get_gallery(self):
        url = f"{self.base_url}/routes/image/gallery"
        headers = self.get_headers()  # includes token if logged in
        
        try:
            response = self.http_client.get(url, headers=headers)
            data = response.json()
        except Exception as e:
            print("Failed to fetch gallery:", e)
            return {"success": False, "message": "Network or parsing error"}

        if not data.get("success"):
            print(f"{data}")
            return data 

        images = data.get("images", [])
        # Now each image dict contains:
        # - likes: total likes
        # - liked_by_user: True/False if current user liked it

        return {"success": True, "images": images}
    
    def like_image(self, image_id: int):
        url = f"{self.base_url}/routes/image/like"
        response = self.http_client.post(url, json={"image_id": image_id}, headers=self.get_headers())
        try:
            data = response.json()
        except Exception:
            print("Response is not JSON. You might need to sign in.")
            return {"success": False, "message": "Invalid response"}

        if data.get("success"):
            self.image_liked.emit()
        else:
            if data.get("message") in ["no token provided.", "invalid token."]:
                print("You need to sign in")
        return data

    def unlike_image(self, image_id: int):
        url = f"{self.base_url}/routes/image/unlike"
        response = self.http_client.post(url, json={"image_id": image_id}, headers=self.get_headers())
        try:
            data = response.json()
        except Exception:
            print("Response is not JSON. You might need to sign in.")
            return {"success": False, "message": "Invalid response"}

        if data.get("success"):
            self.image_unliked.emit()
        else:
            if data.get("message") in ["no token provided.", "invalid token."]:
                print("You need to sign in")
        return data


    def upload_image(self, file_path, filename):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        mime_type, _ = mimetypes.guess_type(file_path)
        mime_type = mime_type or "application/octet-stream"

        url = f"{self.base_url}/routes/image/upload"
        with open(file_path, "rb") as f:
            files = {"image": (os.path.basename(file_path), f, mime_type)}
            data = {"filename": filename}
            response = self.http_client.post(url, headers=self.get_headers(), files=files, data=data)

        print(f"{response}")
        response.raise_for_status()
        self.image_uploaded.emit()
        return response.json()
    
    
