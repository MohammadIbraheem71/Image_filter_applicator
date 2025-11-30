# utils/image_loader.py
from PySide6.QtWidgets import QLabel, QWidget, QGridLayout
from pages.widgets.image_widget import image_widget

class image_loader:
    def __init__(self, container_widget: QWidget, columns: int = 3, api=None):
        self.container = container_widget
        self.layout = self.container.layout()

        if not self.layout:
            self.layout = QGridLayout(self.container)
            self.container.setLayout(self.layout)

        self.columns = columns
        self.api = api  # client_api instance

    def load_images(self, image_items: list):
        # Clear existing images
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        row, col = 0, 0

        for item in image_items:
            # detect type
            if isinstance(item, str):
                image_url = item
                image_id = None
                likes = 0

            elif isinstance(item, dict):
                image_url = item.get("image_url")
                image_id = item.get("id")
                likes = item.get("likes", 0)

            else:
                image_url = str(item)
                image_id = None
                likes = 0
                
            image_card = image_widget(
                url=image_url,
                likes=likes,
                image_id=image_id,
                api=self.api
            )

            self.layout.addWidget(image_card, row, col)
            col += 1

            if col >= self.columns:
                col = 0
                row += 1
