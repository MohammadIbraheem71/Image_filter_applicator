# utils/image_loader.py
from PySide6.QtWidgets import QWidget, QGridLayout
from pages.widgets.image_widget import image_widget
from PySide6.QtCore import Qt, QRectF, QThreadPool, Signal
#this class is responsible for loading image_widgets into the layout grid for the gallery or 
#any other scroll area
#an api object is passed in to manage the loading from db
class image_loader:

    img_magnify_requested = Signal(int)

    def __init__(self, container_widget: QWidget, columns: int = 3, api=None):
        self.container = container_widget
        self.layout = self.container.layout()
        self.container.setLayout(self.layout)
        self.columns = columns
        self.api = api 

        if self.layout is None:
            self.layout = QGridLayout()
            self.container.setLayout(self.layout)

    #utility function to clear all previous images
    def clear_layout(self):
        
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    #this function is responsible for the loading of the images from the client api
    def load_images(self):
        if not self.api:
            raise RuntimeError("API instance not provided.")

        self.clear_layout()

        try:
            gallery_data = self.api.get_gallery()
        except Exception as e:
            print("Failed to fetch gallery:", e)
            return

        if not gallery_data.get("success"):
            print("Error from API:", gallery_data.get("message"))
            return

        images = gallery_data.get("images", [])

        row, col = 0, 0
        for item in images:
            image_url = item.get("image_url")
            image_id = item.get("id")
            likes = item.get("likes", 0)
            liked_by_user = item.get("liked_by_user", False)

            # Create the image widget with like state
            img_card = image_widget(
                url=image_url,
                likes=likes,
                image_id=image_id,
                api=self.api,
                liked_by_user=liked_by_user  # new param for initial state
            )

            # Disable like button if user is not authenticated
            if not getattr(self.api, "token", None):
                img_card.disable_like_button()


            self.layout.addWidget(img_card, row, col)
            col += 1
            if col >= self.columns:
                col = 0
                row += 1
