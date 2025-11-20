# pages/filter_page.py
from PySide6.QtWidgets import QPushButton, QComboBox, QLabel, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PIL import Image

class FilterPage:
    def __init__(self, page_widget, filter_factory, handler):
        self.page = page_widget       # the QWidget from Designer
        self.factory = filter_factory
        self.handler = handler

        # Find widgets in the Designer page
        self.upload_btn = self.page.findChild(QPushButton, "upload_btn")
        self.download_btn = self.page.findChild(QPushButton, "download_btn")
        self.filter_cbx = self.page.findChild(QComboBox, "filter_cbx")
        self.og_img_lbl = self.page.findChild(QLabel, "og_img_lbl")
        self.new_img_lbl = self.page.findChild(QLabel, "new_img_lbl")

        self.filter_cbx.addItem("Select Filter...")  # placeholder
        for name in self.factory.filter_dict.keys():
            self.filter_cbx.addItem(name)
            print(f"added {name} to filter_cbx")

        # Page state
        self.original_image = None
        self.filtered_image = None

        # Disable filter dropdown until image is uploaded
        self.filter_cbx.setEnabled(False)

        # Connect signals
        self.upload_btn.clicked.connect(self.upload_image)
        self.download_btn.clicked.connect(self.download_image)
        self.filter_cbx.currentIndexChanged.connect(self.apply_filter)

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self.page, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if not file_name:
            return
        self.handler.upload_image(file_name)
        self.show_image(self.og_img_lbl, self.handler.image)
        self.filter_cbx.setEnabled(True)

    def apply_filter(self):
        if self.handler.image is None:
            return

        selected_filter = self.filter_cbx.currentText()
        if selected_filter == "Select Filter...":
            return

        filter_obj = self.factory.get_filter(selected_filter)

        #we keep original for insurance
        self.original_image = self.handler.image.copy()

        #we apply the filter to the image and save
        self.filtered_image = filter_obj.apply(self.original_image.copy())
        
        # self.filtered_image = self.filtered_image.resize(
        #     self.original_image.size,
        #     resample=Image.LANCZOS
        # )

        # Show in the label
        self.show_image(self.new_img_lbl, self.filtered_image)
        self.show_image(self.og_img_lbl, self.original_image)
        print(f"original image size = {self.original_image.size}")



    def download_image(self):
        if self.filtered_image is None:
            return
        file_name, _ = QFileDialog.getSaveFileName(
            self.page, "Save Image", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)"
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
        from PySide6.QtGui import QImage, QPixmap
        image = image.convert("RGBA")
        data = image.tobytes("raw", "RGBA")
        qimage = QImage(data, image.width, image.height, QImage.Format_RGBA8888)
        return QPixmap.fromImage(qimage)
