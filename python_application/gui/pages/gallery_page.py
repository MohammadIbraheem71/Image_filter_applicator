# pages/gallery_page.py
from PySide6.QtWidgets import QWidget
from ui_py.gallery_page import Ui_Form  # compiled UI

class gallery_page(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self) 
        
        # Connect signals
        self.ui.upld_glry_btn.clicked.connect(self.upload_gallery)

    def upload_gallery(self):
        print("Upload gallery button clicked")
        # TODO: implement upload logic here
