# image_handler.py
from PIL import Image
import os
from filters.filter_types.base_filter import base_filter
from image_handler.ImageLoader import ImageLoader
from image_handler.ImageSaver import ImageSaver
from image_handler.FilterApplier import FilterApplier

# Optional unified handler if you want one interface:
class image_handler:
    def __init__(self):
        self.image = None
        self.loader = ImageLoader()
        self.saver = ImageSaver()
        self.filterer = FilterApplier()

    def upload_image(self, path: str):
        self.image = self.loader.load(path)

    def apply_filter(self, filter_obj: base_filter):
        self.image = self.filterer.apply(self.image, filter_obj)

    def download_image(self, path: str):
        self.saver.save(self.image, path)

    def clear_image(self):
        self.image = None
