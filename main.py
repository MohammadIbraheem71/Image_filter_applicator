#testing goes on in here
from image_handler import image_handler
from filter_factory import filter_factory
from filters.blur_filter import blur_filter
from filters.edge_filter import edge_filter
from filters.grayscale_filter import grayscale_filter

filter_fac_obj = filter_factory()

filter_fac_obj.add_filter("blur", blur_filter())
filter_fac_obj.add_filter("edge", edge_filter())
filter_fac_obj.add_filter("grayscale", grayscale_filter())

handler = image_handler()

handler.upload_image("test_images/bateman.PNG")
handler.apply_filter(filter_fac_obj.get_filter("edge"))
handler.download_image("test_images/test.png")