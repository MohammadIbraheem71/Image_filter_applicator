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
from image_handler.image_handler import image_handler


class FrontPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.original_image = None
        self.filtered_image = None
        

        self.handler = image_handler()

        self.factory = filter_factory()
        self.factory.add_filter("blur", blur_filter())
        self.factory.add_filter("edge", edge_filter())
        self.factory.add_filter("sepia", sepia_filter())
        self.factory.add_filter("grayscale", grayscale_filter())
        

        # Set default selected index to placeholder
        self.ui.filter_dropdown.model().item(0).setEnabled(False)
        self.ui.filter_dropdown.setCurrentIndex(0)
        self.ui.filter_dropdown.setEnabled(False) 

        # Connect buttons
        self.ui.upload_image.clicked.connect(self.upload_image)
        self.ui.filter_dropdown.currentIndexChanged.connect(self.apply_filter)
        self.ui.download_image.clicked.connect(self.download_image)

        

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if not file_name:
            return

        try:
            self.handler.upload_image(file_name)
            self.show_image(self.ui.image_preview, self.handler.image)

            # Enable dropdown after image upload
            self.ui.filter_dropdown.setEnabled(True)
        except Exception as e:
            print("Error uploading image:", e)

    def show_image(self, label, pil_image):
        if pil_image:
            pixmap = self.pil_to_qpixmap(pil_image)
            scaled = pixmap.scaled(
                label.width(),
                label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            label.setPixmap(scaled)

    def apply_filter(self):
        if self.handler.image is None:
            return

        selected_filter = self.ui.filter_dropdown.currentText()
        filter_obj = self.factory.get_filter(selected_filter)

        if selected_filter == "Select Filter...":
            return

        try:
            self.original_image = self.handler.image.copy()
            self.filtered_image = filter_obj.apply(self.original_image)

            
            self.show_image(self.ui.new_image_preview, self.filtered_image)
        except Exception as e:
            print("Error applying filter:", e)


    def download_image(self):
        if self.filtered_image is None:
            return

        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)"
        )
        if file_name:
            try:
                self.handler.image = self.filtered_image
                self.handler.download_image(file_name)
                self.handler.image = self.original_image
            except Exception as e:
                print("Error saving image:", e)

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
