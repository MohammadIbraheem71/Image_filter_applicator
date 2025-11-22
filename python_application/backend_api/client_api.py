import requests
import mimetypes
import os

#creating an interface to the backend here, uses the backend routs 
class client_api:
    #base url used to define the url of the backend, u know what i mean excuse my english
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        
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
            
            return True
        else:
            print("invalid credentials")
            
            return False
    
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
    def upload_image(self, file_path, original_name):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Extract original filename
        original_name = os.path.basename(file_path)

        # Guess MIME type (default to application/octet-stream if unknown)
        mime_type, _ = mimetypes.guess_type(file_path)
        if not mime_type:
            mime_type = "application/octet-stream"

        url = f"{self.base_url}/upload"  # matches your backend route

        with open(file_path, "rb") as f:
            files = {
                "image": (original_name, f, mime_type)
            }
            response = requests.post(url, headers=self.get_headers(), files=files)

        # Raise exception if upload failed
        response.raise_for_status()
        return response.json()
        
    #this function registers a new user
    #user has to log in once signed up so the api stores its token
    def signup(self, username, email, password):
        url = f"{self.base_url}/routes/auth/signup"
        response = requests.post(url, json={
            "email": email,
            "password": password
        })

        if response.status_code == 201:  # usually 201 Created
            data = response.json()
            print(f"User '{email}' signed up successfully")
            return True
        else:
            print("Signup failed")
            return False
