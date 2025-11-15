import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from PIL import Image, ImageFilter
from app_gui import Ui_MainWindow  # the converted file

class ImageFilterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Data
        self.pil_image = None

        # Connect buttons
        self.ui.load_button.clicked.connect(self.load_image)
        # self.ui.filterButton.clicked.connect(self.apply_filter)
        # self.ui.saveButton.clicked.connect(self.save_image)

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            self.pil_image = Image.open(file_name)
            self.show_image()

    def show_image(self):
        if self.pil_image:
            qt_image = self.pil_to_qpixmap(self.pil_image)
            self.ui.image_label.setPixmap(qt_image.scaled(
                self.ui.image_label.width(), self.ui.image_label.height()
            ))
            
    @staticmethod
    def pil_to_qpixmap(image):
        image = image.convert("RGBA")
        data = image.tobytes("raw", "RGBA")
        from PySide6.QtGui import QImage, QPixmap
        qimage = QImage(data, image.width, image.height, QImage.Format_RGBA8888)
        return QPixmap.fromImage(qimage)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageFilterApp()
    window.show()
    sys.exit(app.exec())
