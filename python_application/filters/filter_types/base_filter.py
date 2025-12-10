# base_filter.py
from PIL import Image

#a base class for filters
#must be implmeented by childer
class base_filter:
    def apply(self, image: Image.Image) -> Image.Image:
        raise NotImplementedError("Subclasses must implement the apply() method.")
