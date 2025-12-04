import requests
import mimetypes
import os
from PySide6.QtCore import QObject, Signal

class GalleryAPI(QObject):
    image_uploaded = Signal()
    image_liked = Signal()   # new signal
    image_unliked = Signal() 
    image_deleted = Signal()

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
    
        #this function gets the users gallery only
    
    
    def get_user_gallery(self):
        url = f"{self.base_url}/routes/image/user_gallery"
        headers = self.get_headers()  # includes token if logged in

        try:
            response = self.http_client.get(url, headers=headers)
            data = response.json()
        except Exception as e:
            print("Failed to fetch user gallery:", e)
            return {"success": False, "message": "Network or parsing error"}

        if not data.get("success"):
            print(f"{data}")
            return data

        images = data.get("images", [])
        # each image includes:
        # - likes
        # - liked_by_user
        # - image_url, filename, id, etc.

        return {
            "success": True,
            "images": images
        }

    #this fetches a single image and its meta data, given the image id
    def get_image(self, image_id: int):
        url = f"{self.base_url}/routes/image/get_single_img/{image_id}"
        headers = self.get_headers()  # token included if logged in

        try:
            response = self.http_client.get(url, headers=headers)
        except Exception as e:
            print(f"Network error while fetching image {image_id}:", e)
            return {"success": False, "message": "Network error"}

        try:
            data = response.json()
        except Exception:
            print("Invalid JSON received from server.")
            return {"success": False, "message": "Invalid server response"}

        if not data.get("success"):
            print(f"Error fetching image: {data}")
            return data
        
        # Expected backend structure:
        # {
        #   "success": true,
        #   "image": { ...full metadata... }
        # }

        return {
            "success": True,
            "image": data.get("image")
        }

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
    
    def delete_image(self, image_id: int):
        if not self.token:
            print("You must be signed in to delete an image.")
            return {"success": False, "message": "Not authenticated"}
        
        url = f"{self.base_url}/routes/image/delete/{image_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = requests.delete(url, headers=headers)
        except Exception as e:
            print(f"Network error while deleting image {image_id}:", e)
            return {"success": False, "message": "Network error"}
        
        # Check HTTP status code
        if response.status_code == 404:
            print(f"Image {image_id} not found.")
            return {"success": False, "message": "Image not found"}
        
        if response.status_code == 500:
            try:
                data = response.json()
                error_msg = data.get("error", "Server error")
            except Exception:
                error_msg = "Server error"
            print(f"Server error while deleting image {image_id}:", error_msg)
            return {"success": False, "message": error_msg}
        
        # Handle successful deletion (status 200)
        if response.status_code == 200:
            try:
                data = response.json()
                message = data.get("message", "Deleted successfully")
                print(f"Image {image_id} deleted successfully.")
                # Emit signal to update UI
                self.image_deleted.emit()
                return {"success": True, "message": message}
            except Exception:
                print("Invalid JSON received from server during delete.")
                return {"success": False, "message": "Invalid server response"}
        
        # Handle any other unexpected status codes
        print(f"Unexpected response status {response.status_code} while deleting image.")
        return {"success": False, "message": f"Unexpected error (status {response.status_code})"}

