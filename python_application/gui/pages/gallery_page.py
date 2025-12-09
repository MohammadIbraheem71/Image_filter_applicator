# pages/gallery_page.py
from PySide6.QtWidgets import QWidget, QSizePolicy
from ui_py.gallery_page import Ui_gallery_pg
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from backend_api.client_api import client_api
from pages.dialog_boxes.upload_dialog import upload_dialog
from pages.gallery_grid import gallery_grid
from utils.image_loader import image_loader
from pages.widgets.image_widget import image_widget
from pages.widgets.image_widget_trash import image_widget_trash


class gallery_page(QWidget):
    def __init__(self, api: client_api):
        super().__init__()
        self.ui = Ui_gallery_pg()
        self.ui.setupUi(self)
        self.api = api

        self.loader = image_loader(self.ui.image_grid, columns=2, api=self.api, widget_cls=image_widget)
        #load gallery images
        self.refresh_gallery()

        
        self.api.image_uploaded.connect(self.refresh_gallery) #refresh when image is loaded

        self.ui.upld_glry_btn.clicked.connect(self.upload_to_gallery)
        

    def refresh_gallery(self):
        try:
            data = self.api.get_gallery()  # fetch from /gallery route
            images_list = data.get("images", [])  # make sure this matches backend JSON
            # Pass the list of dicts directly, not just URLs
            layout = self.ui.image_grid.layout()
            if layout is None:
                from PySide6.QtWidgets import QGridLayout
                layout = QGridLayout(self.ui.image_grid)
                self.ui.image_grid.setLayout(layout)

            #clear any exiting widgets to prevent interference
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.setParent(None)

            if images_list:
                self.ui.no_upload_lbl.hide()
                #load images if list is not empty
                self.loader.load_images(images=images_list)
            else:
                # show the no_upload_lbl which is the error msg if no imgs are uploded
                self.ui.no_upload_lbl.show()
        except Exception as e:
            print("Error fetching gallery:", e)


    def upload_to_gallery(self):
        upload_dlg = upload_dialog(api=self.api, parent=self)
        if upload_dlg.exec():
            #refresh gallery after successful upload
            self.refresh_gallery()
            

    def open_magnified_view(self, image_id: int):
        # Example:
        data = self.api.get_image(image_id)
        if not data.get("success"):
            print("Failed to fetch image details:", data.get("message"))
            return

        image_data = data.get("image")  # the full image info from backend
        
        print(f"Open magnified view for image ID: {image_id}")
