from PIL import Image
import os
from filters.filter_types.base_filter import base_filter


class FilterApplier:
    """Applies filters to images."""
    def apply(self, image: Image.Image, filter_obj: base_filter) -> Image.Image:
        if image is None:
            raise ValueError("No image loaded")
        try:
            return filter_obj.apply(image)
        except Exception as e:
            raise Exception(f"Error applying filter: {e}")
