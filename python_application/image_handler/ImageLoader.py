from PIL import Image
import os

class ImageLoader:
    """Handles loading images from disk."""
    def load(self, file_path: str) -> Image.Image:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        try:
            return Image.open(file_path)
        except Exception as e:
            raise Exception(f"Error loading image: {e}")
