from PIL import Image
import os

#saves images to disk
class ImageSaver:
    
    def save(self, image: Image.Image, save_path: str):
        if image is None:
            raise ValueError("No image to save")
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        try:
            image.save(save_path)
        except Exception as e:
            raise Exception(f"Error saving image: {e}")
