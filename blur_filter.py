from PIL import Image, ImageFilter
from base_filter import base_filter

class blur_filter(base_filter):
    def apply(self, image: Image.Image) -> Image.Image:
        return image.filter(ImageFilter.BLUR)
