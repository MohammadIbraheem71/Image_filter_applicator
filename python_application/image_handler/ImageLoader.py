from PIL import Image
import os

#handles loading images form disks
class ImageLoader:
    
    def load(self, file_path: str) -> Image.Image:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        try:
            return Image.open(file_path)
        except Exception as e:
            raise Exception(f"Error loading image: {e}")
