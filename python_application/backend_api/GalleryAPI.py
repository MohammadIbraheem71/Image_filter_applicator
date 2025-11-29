import requests
import mimetypes
import os
from PySide6.QtCore import QObject, Signal

class GalleryAPI(QObject):
    image_uploaded = Signal()

    def __init__(self, base_url, token=None, http_client=requests):
        super().__init__()
        self.base_url = base_url
        self.token = token
        self.http_client = http_client

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def get_gallery(self):
        url = f"{self.base_url}/routes/image/gallery"
        response = self.http_client.get(url)
        return response.json()

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

        response.raise_for_status()
        self.image_uploaded.emit()
        return response.json()
