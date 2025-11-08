# sepia_filter.py
from PIL import Image
import numpy as np
from filters.base_filter import Filter

class SepiaFilter(Filter):
    """Applies a sepia tone to the image."""

    def apply(self, image: Image.Image) -> Image.Image:
        # Ensure image is RGB
        sepia_image = np.array(image.convert("RGB"), dtype=np.float64)

        # Split into RGB channels
        r, g, b = sepia_image[..., 0], sepia_image[..., 1], sepia_image[..., 2]

        # Apply sepia color transformation
        tr = 0.393 * r + 0.769 * g + 0.189 * b
        tg = 0.349 * r + 0.686 * g + 0.168 * b
        tb = 0.272 * r + 0.534 * g + 0.131 * b

        # Clip to 0–255 range
        sepia_image[..., 0] = np.clip(tr, 0, 255)
        sepia_image[..., 1] = np.clip(tg, 0, 255)
        sepia_image[..., 2] = np.clip(tb, 0, 255)

        # Convert back to PIL Image (ensuring RGB mode)
        return Image.fromarray(sepia_image.astype(np.uint8), "RGB")
 