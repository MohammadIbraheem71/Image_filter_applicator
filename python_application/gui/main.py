import sys
import os

# Add project root to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PIL import Image, ImageFilter
from app_gui import Ui_MainWindow

from filters.filter_factory import filter_factory
from filters.filter_types.blur_filter import blur_filter
from filters.filter_types.sepia_filter import sepia_filter
from filters.filter_types.edge_filter import edge_filter
from filters.filter_types.grayscale_filter import grayscale_filter


class FrontPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pil_image = None

        self.factory = filter_factory()
        self.factory.add_filter("blur", blur_filter())
        self.factory.add_filter("edge", edge_filter())
        self.factory.add_filter("sepia", sepia_filter())
        self.factory.add_filter("grayscale", grayscale_filter())
        
        # Connect buttons
        self.ui.upload_image.clicked.connect(self.upload_image)
        self.ui.apply_filter.clicked.connect(self.apply_filter)
        self.ui.download_image.clicked.connect(self.download_image)

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if not file_name:
            return

        self.pil_image = Image.open(file_name)
        self.show_image(self.ui.image_preview)

    def show_image(self, label):
        if self.pil_image:
            pixmap = self.pil_to_qpixmap(self.pil_image)
            scaled = pixmap.scaled(
                label.width(),
                label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            label.setPixmap(scaled)

    def apply_filter(self):
        if not self.pil_image:
            return

        # Example filter — replace with your SDA filters
        self.pil_image = self.pil_image.filter(ImageFilter.BLUR)
        self.show_image(self.ui.new_image_preview)

    def download_image(self):
        if not self.pil_image:
            return

        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)"
        )
        if file_name:
            self.pil_image.save(file_name)

    @staticmethod
    def pil_to_qpixmap(image):
        from PySide6.QtGui import QImage, QPixmap
        image = image.convert("RGBA")
        data = image.tobytes("raw", "RGBA")
        qimage = QImage(data, image.width, image.height, QImage.Format_RGBA8888)
        return QPixmap.fromImage(qimage)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FrontPage()
    window.show()
    sys.exit(app.exec())
