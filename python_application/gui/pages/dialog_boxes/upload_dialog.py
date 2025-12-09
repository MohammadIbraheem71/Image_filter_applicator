from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from ui_py.upload_dialog import Ui_upload_dialog
import os
from backend_api.client_api import client_api

class upload_dialog(QDialog):
    def __init__(self, api: client_api, parent=None):
        super().__init__(parent)
        self.ui = Ui_upload_dialog()
        self.ui.setupUi(self)
        self.api = api
        self.selected_file = None

        # Hide error and success label initially
        self.ui.error_lbl.setVisible(False)
        self.ui.error_lbl.setText("")
        self.ui.success_lbl.setVisible(False)
        self.ui.success_lbl.setText("")

        self.ui.select_img_btn.clicked.connect(self.clear_errors)
        self.ui.description_edt.textChanged.connect(self.clear_errors)

        # Connect buttons
        self.ui.select_img_btn.clicked.connect(self.choose_file)
        self.ui.upload_btn.clicked.connect(self.upload_file)
    def show_error(self, text: str):
        self.ui.error_lbl.setText(text)
        self.ui.error_lbl.setVisible(True)
    
    def clear_errors(self):
        self.ui.error_lbl.setVisible(False)
        self.ui.error_lbl.setText("")
        self.ui.success_lbl.setVisible(False)
        self.ui.success_lbl.setText("")

    def show_success(self, text: str):
        """Display success message inline."""
        self.ui.success_lbl.setText(text)
        self.ui.success_lbl.setVisible(True)
        self.ui.error_lbl.setVisible(False)

    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            self.selected_file = file_path

            #loadng the preview
            pixmap = QPixmap(file_path)
            pixmap = pixmap.scaled(
                self.ui.img_lbl.width(),
                self.ui.img_lbl.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.ui.img_lbl.setPixmap(pixmap)

            #clear previous errors
            self.ui.error_lbl.setVisible(False)
            self.ui.error_lbl.setText("")

    def upload_file(self):
        filename = self.ui.description_edt.text().strip()

        #validation errors → error_lbl
        if not self.selected_file:
            self.show_error("Please choose an image file.")
            return

        if not filename:
            self.show_error("Please enter a short description.")
            return

        try:
            result = self.api.upload_image(self.selected_file, filename)

            # if unauthorizedd, show following error
            if isinstance(result, dict) and result.get("status") == "unauthorized":
                self.show_error("Unauthorized. Please login again.")
                return

            #the SUCCESS popup
            self.show_success("Image uploaded successfully!")

        except Exception as e:
            #try to extract HTTP status code if available
            words = str(e).strip().split(' ')

            if '401' in words or '403' in words:
                self.show_error("Unauthorized. Please login.")
            else:
                self.show_error(f"Upload failed: {str(e)}")
