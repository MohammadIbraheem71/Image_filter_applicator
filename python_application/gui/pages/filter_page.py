# pages/filter_page.py
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PIL import Image
from ui_py.filter_gui import Ui_filter_pg 

class FilterPage(QWidget):
    def __init__(self, filter_factory, handler):
        super().__init__()
        # Setup UI
        self.ui = Ui_filter_pg()
        self.ui.setupUi(self)

        self.factory = filter_factory
        self.handler = handler

        #ppopulate filter combo box
        self.ui.filter_cbx.addItem("Select Filter...")  # placeholder
        for name in self.factory.filter_dict.keys():
            self.ui.filter_cbx.addItem(name)
            print(f"added {name} to filter_cbx")

        #page state
        self.original_image = None
        self.filtered_image = None

        #disable filter dropdown until image is uploaded
        self.ui.filter_cbx.setEnabled(False)

        #connecting buttons
        self.ui.upload_btn.clicked.connect(self.upload_image)
        self.ui.download_btn.clicked.connect(self.download_image)
        self.ui.filter_cbx.currentIndexChanged.connect(self.apply_filter)

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if not file_name:
            return
        self.handler.upload_image(file_name)
        self.show_image(self.ui.og_img_lbl, self.handler.image)
        self.ui.filter_cbx.setEnabled(True)

    def apply_filter(self):
        if self.handler.image is None:
            return

        selected_filter = self.ui.filter_cbx.currentText()
        if selected_filter == "Select Filter...":
            return

        filter_obj = self.factory.get_filter(selected_filter)

        #keep original for insurance
        self.original_image = self.handler.image.copy()

        #apply filter
        self.filtered_image = filter_obj.apply(self.original_image.copy())

        #show images
        self.show_image(self.ui.new_img_lbl, self.filtered_image)
        self.show_image(self.ui.og_img_lbl, self.original_image)
        print(f"original image size = {self.original_image.size}")

    def download_image(self):
        if self.filtered_image is None:
            return
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)"
        )
        if file_name:
            self.handler.image = self.filtered_image
            self.handler.download_image(file_name)
            self.handler.image = self.original_image

    def show_image(self, label, pil_image):
        if pil_image:
            pixmap = self.pil_to_qpixmap(pil_image)
            scaled = pixmap.scaled(
                label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            label.setPixmap(scaled)
            print(f"width = {label.width()}, height = {label.height()}")

    @staticmethod
    def pil_to_qpixmap(image):
        image = image.convert("RGBA")
        data = image.tobytes("raw", "RGBA")
        qimage = QImage(data, image.width, image.height, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

