from PySide6.QtWidgets import QDialog, QFileDialog,QMessageBox
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

        # Connect buttons
        self.ui.choose_img_btn.clicked.connect(self.choose_file)
        self.ui.upload_btn.clicked.connect(self.upload_file)
        self.ui.cancel_btn.clicked.connect(self.reject)

    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            self.selected_file = file_path


            # Load and display preview
            pixmap = QPixmap(file_path)
            # Scale to fit the label while keeping aspect ratio
            pixmap = pixmap.scaled(
                self.ui.preview_lbl.width(),
                self.ui.preview_lbl.height(),
                Qt.KeepAspectRatio,        # aspect mode
                Qt.SmoothTransformation    # transformation mode (optional)
            )
            self.ui.preview_lbl.setPixmap(pixmap)

    def upload_file(self):
        filename = self.ui.description_edt.text().strip()
        
        if not self.selected_file or not filename:
            QMessageBox.warning(self, "Missing", "choose a file and enter a short description!")
            return
        
        print(f"filename: {filename}")
        try:
            self.api.upload_image(self.selected_file, filename)
            
            
             # SUCCESS POPUP
            QMessageBox.information(self, "Upload Successful",
                                    "image uploaded successfully!")
            self.accept()  # Close dialog
            
        except Exception as e:
            self.ui.progress_bar.setVisible(False)
            QMessageBox.critical(self, "Upload Failed", f"Error: {str(e)}")
