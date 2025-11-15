from PIL import Image, ImageFilter
from filters.filter_types.base_filter import base_filter

class edge_filter(base_filter):
    def apply(self, image: Image.Image) -> Image.Image:
        image = image.convert("L")
        #image.show()
        edges= image.filter(ImageFilter.FIND_EDGES)
        #edges.show()
        
        return edges
