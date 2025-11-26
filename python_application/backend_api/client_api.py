import requests
import mimetypes
import os
from PySide6.QtCore import QObject, Signal

#creating an interface to the backend here, uses the backend routs 
class client_api(QObject):
    image_uploaded = Signal()

    #base url used to define the url of the backend, u know what i mean excuse my english
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.token = None
        self.user_info = None
        
    #verifies the user's log in
    def login(self, email, password):
        url = f"{self.base_url}/routes/auth/login"
        
        response = requests.post(url, json = {
            "email": email, 
            "password" : password
        })
        
        if response.status_code == 200:
            print("user logged in sucessfully")
            data = response.json()
            self.token = data["token"]
            self.user_info = data["user"]

            return True
        else:
            data = response.json()
            error_msg = data.get("error", "")

            if "verify your email" in error_msg.lower():
                print("email not verified")
                return "unverified"  # special return value for unverified email
            else:
                print("invalid credentials")
                return False  # treat wrong credentials as failure
    
    #get shared gallery function
    def get_gallery(self):
        url = f"{self.base_url}/routes/upload/gallery"
        response = requests.get(url)
        return response.json()
    
    #this function is used for authentication
    def get_headers(self):
        if not self.token:
            return {}
        else:
            return {"Authorization" : f"Bearer {self.token}"}
        
    #function to upload to the shared gallery, uses the get_headers function
    #as authentication is requried for the upload func
    def upload_image(self, file_path, filename):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Extract original filename
        original_name = os.path.basename(file_path)

        # Guess MIME type (default to application/octet-stream if unknown)
        mime_type, _ = mimetypes.guess_type(file_path)
        if not mime_type:
            mime_type = "application/octet-stream"

        url = f"{self.base_url}/routes/image/upload"  # matches your backend route

        with open(file_path, "rb") as f:
            files = {
                "image": (original_name, f, mime_type)
            }
            
            data = {
                "filename": filename
            }
            response = requests.post(url, headers=self.get_headers(), files=files, data = data)
            

        # Raise exception if upload failed
        response.raise_for_status()

        self.image_uploaded.emit()

        return response.json()
        
    #this function registers a new user
    #user has to log in once signed up so the api stores its token
    def signup(self, username, email, password):
        url = f"{self.base_url}/routes/auth/signup"
        try:
            response = requests.post(url, json={
                "username": username, 
                "email": email,
                "password": password
            })

            if response.status_code == 201:  # Success
                print(f"User '{email}' signed up successfully")
                return True, None  # success, no error
            else:
                # Extract error message from backend
                try:
                    data = response.json()
                    error_msg = data.get("error", "Unknown error")
                except Exception:
                    error_msg = response.text or "Unknown error"

                print(f"Signup failed: {error_msg}")
                return False, error_msg  # failure + error message

        except requests.RequestException as e:
            print(f"Network error: {e}")
            return False, str(e)

