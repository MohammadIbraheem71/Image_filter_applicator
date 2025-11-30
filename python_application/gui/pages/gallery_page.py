# pages/gallery_page.py
from PySide6.QtWidgets import QWidget, QSizePolicy
from ui_py.gallery_page import Ui_gallery_pg
from backend_api.client_api import client_api
from pages.dialog_boxes.upload_dialog import upload_dialog
from pages.gallery_grid import gallery_grid
from utils.image_loader import image_loader

class gallery_page(QWidget):
    def __init__(self, api: client_api):
        super().__init__()
        self.ui = Ui_gallery_pg()
        self.ui.setupUi(self)
        self.api = api

        self.loader = image_loader(self.ui.image_grid, columns=2, api=self.api)

        # Connect signals
        self.ui.upld_glry_btn.clicked.connect(self.upload_to_gallery)
        

        # Load gallery images
        self.refresh_gallery()
        

    def refresh_gallery(self):
        try:
            data = self.api.get_gallery()  # fetch from /gallery route
            images_list = data.get("images", [])  # make sure this matches backend JSON
            # Pass the list of dicts directly, not just URLs
            self.loader.load_images()
        except Exception as e:
            print("Error fetching gallery:", e)

    def upload_to_gallery(self):
        upload_dlg = upload_dialog(api=self.api, parent=self)
        if upload_dlg.exec():
            # Refresh gallery after successful upload
            self.refresh_gallery()
