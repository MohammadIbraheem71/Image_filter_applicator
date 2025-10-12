from PIL import Image
import os

class image_handler:
    def __init__(self):
        self.image = None
        
    def upload_image(self, file_path: str):
        if not os.path.exists(file_path):
            raise Exception(f"file: {file_path} not found")
            return
        
        try:
            self.image = Image.open(file_path)
        except Exception as e:
            raise Exception(f"error uploading image: {e}")
        
    def apply_filter(self, filter_obj):
        if self.image is None:
            raise Exception("there is no image loaded")
        
        try:
            self.image = filter_obj.apply(self.image)
        except Exception as e:
            raise Exception(f"error applying filter: {e}")
        
    def download_image(self, save_path: str):
        
        if self.image is None:
            raise Exception("there is no image loaded")
        
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        try:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            self.image.save(save_path)
        except Exception as e:
            raise Exception(f"error saving image: {e}")
        
    def clear_image(self):
        self.Image = None
        