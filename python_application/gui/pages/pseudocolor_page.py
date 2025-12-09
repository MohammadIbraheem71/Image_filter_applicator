# pages/pseudocolor_page.py
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from ui_py.pseudocolor_page import Ui_pseudoclr_pg
from pseudocolor.colorization import colorize_image
from PIL.ImageQt import ImageQt

class pseudocolor_page(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_pseudoclr_pg()
        self.ui.setupUi(self)

        #store PIL images
        self.gray_img = None
        self.color_img = None
        self.enhanced_img = None

        #connect buttons
        self.ui.upload_btn.clicked.connect(self.upload_image)
        self.ui.download_btn.clicked.connect(self.download_image)

    def upload_image(self):
        #open file dialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Grayscale Image", "", "Images (*.png *.jpg *.jpeg)")
        if not file_path:
            return

        try:
            #colorize image
            self.gray_img, self.enhanced_img = colorize_image(file_path)

            #display original grayscale
            qt_gray = ImageQt(self.gray_img)
            pixmap_gray = QPixmap.fromImage(qt_gray)
            self.ui.old_img_lbl.setPixmap(pixmap_gray.scaled(
                self.ui.old_img_lbl.width(),
                self.ui.old_img_lbl.height(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

            #display enhanced colorized
            qt_enhanced = ImageQt(self.enhanced_img)
            pixmap_enhanced = QPixmap.fromImage(qt_enhanced)
            self.ui.new_img_lbl.setPixmap(pixmap_enhanced.scaled(
                self.ui.new_img_lbl.width(),
                self.ui.new_img_lbl.height(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to colorize image:\n{e}")

    def download_image(self):
        if not self.enhanced_img:
            QMessageBox.warning(self, "No Image", "Please upload and colorize an image first!")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Save Enhanced Image", "", "PNG Image (*.png);;JPEG Image (*.jpg *.jpeg)")
        if not save_path:
            return

        try:
            self.enhanced_img.save(save_path)
            QMessageBox.information(self, "Saved", f"Enhanced image saved to:\n{save_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save image:\n{e}")
