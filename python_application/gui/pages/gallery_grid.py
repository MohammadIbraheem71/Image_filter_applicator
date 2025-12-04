from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from ui_py.image_grid import Ui_image_gallery_grid

#this doesnt seem to be used anywhere yet

class gallery_grid(QWidget, Ui_image_gallery_grid):
    def __init__(self, parent=None):
        print("here")
        super().__init__(parent)
        self.setupUi(self)

        # Store dynamic row/column position
        self.row = 0
        self.col = 0
        self.max_columns = 3  # change as you like

    def add_image(self, image_path: str):
        """
        Adds a single image to the grid layout.
        """
        pixmap = QPixmap(image_path)

        img_label = QLabel()
        img_label.setPixmap(pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        img_label.setAlignment(Qt.AlignCenter)

        # Add label to the next grid cell
        self.gridLayout.addWidget(img_label, self.row, self.col)

        # Advance grid position
        self.col += 1
        if self.col >= self.max_columns:
            self.col = 0
            self.row += 1
