from PySide6.QtCore import QObject, Signal
from backend_api.AuthAPI import AuthAPI
from backend_api.GalleryAPI import GalleryAPI


class client_api(QObject):
    image_uploaded = Signal()

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.token = None
        self.user_info = None
        
    #verifies the user's log in
    def login(self, email, password):
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
    
    def request_password_reset(self, email):
        return self.auth.request_password_reset(email)

    def reset_password(self, token, new_password):
        return self.auth.reset_password(token, new_password)

    # ---------- Gallery methods ----------
    def get_gallery(self):
        return self.gallery.get_gallery()

    def upload_image(self, file_path, filename):
        return self.gallery.upload_image(file_path, filename)
