from PIL import Image
import os

class image_handler:
    def __init__(self):
        self.image = None
        
    def upload_image(self, file_path: str):
        if not os.path.exists(file_path):
            raise Exception(f"file: {file_path} not found")
            return
        
        self.image = Image.open(file_path)
        
    def apply_filter(self, filter_obj):
        if self.image is None:
            raise Exception("there is no image loaded")
        self.image = filter_obj.apply(self.image)
        
    def download_image(self, save_path: str):
        if not os.path.exists(save_path):
            raise Exception(f"file: {save_path} not found")
            return
        self.image.save(save_path)
        
    def clear_image(self):
        self.Image = None
        