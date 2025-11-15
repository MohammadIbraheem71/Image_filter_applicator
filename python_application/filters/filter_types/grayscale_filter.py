from PIL import Image
from filters.filter_types.base_filter import base_filter

class grayscale_filter(base_filter):
    def apply(self, image: Image.Image) -> Image.Image:
        return image.convert("L") 
