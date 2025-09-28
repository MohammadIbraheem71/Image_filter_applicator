from PIL import Image, ImageFilter

image = Image.open("test_images/bateman.PNG")

filtered_image = image.filter(filter = ImageFilter.EDGE_ENHANCE_MORE)

image.show()
filtered_image.show()