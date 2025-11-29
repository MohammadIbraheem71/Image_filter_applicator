# utils/image_loader.py
from PySide6.QtWidgets import QLabel, QWidget, QGridLayout
from PySide6.QtGui import QPixmap
import requests
from io import BytesIO
from pages.widgets.image_widget import image_widget

class image_loader:
    def __init__(self, container_widget: QWidget, columns: int = 3):
        """
        container_widget: QWidget that has a grid layout
        columns: number of images per row
        """
        self.container = container_widget
        self.layout = self.container.layout()

        # Ensure the container has a QGridLayout
        if not self.container.layout():
            self.layout = QGridLayout(self.container)
            self.container.setLayout(self.layout)

        self.columns = columns

    def load_images(self, image_urls: list):
        # Clear existing images
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Add images in grid
        row, col = 0, 0
        for img in image_urls:
            image_card = image_widget(url=img, likes=0)

            self.layout.addWidget(image_card, row, col)
            col += 1
            if col >= self.columns:
                col = 0
                row += 1
