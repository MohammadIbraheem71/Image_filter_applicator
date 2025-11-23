# pages/gallery_page.py
from PySide6.QtWidgets import QWidget
from ui_py.gallery_page import Ui_gallery_pg
from backend_api.client_api import client_api
from pages.dialog_boxes.upload_dialog import upload_dialog

class gallery_page(QWidget):
    def __init__(self, api: client_api ):
        super().__init__()
        self.ui = Ui_gallery_pg()
        self.ui.setupUi(self) 
        self.api = api
        # Connect signals
        self.ui.upld_glry_btn.clicked.connect(self.upload_to_gallery)

    #we open the upload dialog box
    def upload_to_gallery(self):
        upload_dlg = upload_dialog(self.api, parent = self)
        upload_dlg.exec()
        
