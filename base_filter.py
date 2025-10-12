# base_filter.py
from PIL import Image

class BaseFilter:
    """Abstract base class for all filters."""
    def apply(self, image: Image.Image) -> Image.Image:
        raise NotImplementedError("Subclasses must implement the apply() method.")
