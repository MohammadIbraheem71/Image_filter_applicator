# pages/profile_logged_page.py
import requests
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from ui_py.profile_logged_page import Ui_profile_logged_page
from backend_api.client_api import client_api
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout
from utils.image_loader import image_loader
from pages.widgets.image_widget_trash import image_widget_trash
from utils.event_listner import event_listner
from PySide6.QtCore import Qt


#this is the profile logged page
class profile_logged_page(QWidget):

    logout_requested = Signal()

    def __init__(self, api_client: client_api):
        super().__init__()

        self.api = api_client

        self.ui = Ui_profile_logged_page()
        self.ui.setupUi(self)

        self.loader = image_loader(self.ui.image_grid, columns=2, api=self.api, widget_cls=image_widget_trash)
        
        #the Buttons are defined heree
        self.ui.logout_btn.clicked.connect(self.logout)

        self.delete_listner = event_listner(event_name="request_delete", callback=self.delete_image)

        #connecting the buttons to refresh events so that there is autorefresh when an event occurss
        self.api.image_uploaded.connect(self.refresh_user_page)
        self.api.image_liked.connect(self.refresh_user_page)
        self.api.image_unliked.connect(self.refresh_user_page)
        self.api.image_deleted.connect(self.refresh_user_page)
        self.refresh_user_page()
        self.refresh_gallery()

    #this function deletes an image
    def delete_image(self, payload):
        print("deleting image")
        image_id = payload.get("image_id")
        if image_id == None:
            print("no image_id provided, cannot delete.")
            return
        
        self.api.delete_user_image(image_id = image_id)

    #this functions loads the user's images into the gallery
    def refresh_gallery(self):
        try:
            data = self.api.get_user_gallery()  # fetch from /gallery route
            images_list = data.get("images", [])  # make sure this matches backend JSON
            # Pass the list of dicts directly, not just URLs
            
            #get/create layout
            layout = self.ui.image_grid.layout()
            if layout is None:
                from PySide6.QtWidgets import QGridLayout
                layout = QGridLayout(self.ui.image_grid)
                self.ui.image_grid.setLayout(layout)

            #clearing the existing widgets so refresh works proerly
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.setParent(None)

            #conditions if images_list empty or not empty
            if images_list:
                self.ui.no_upload_lbl.hide()
                
                #load images if images are prsnt in gallery
                self.loader.load_images(images=images_list)
            else:
                # Show empty message if truly empty
                self.ui.no_upload_lbl.show()
            
        except Exception as e:
            print("Error fetching gallery:", e)


    #we handle the logout here
    def logout(self):
        self.logout_requested.emit()

    #we load the user info here
    def refresh_user_page(self):
        if not self.api.token:
            return

        # getting the users informationn
        email = self.api.user_info.get("email", "Unknown")
        username = self.api.user_info.get("username", "User")
        verified = self.api.user_info.get("is_verified", 0)

        self.ui.email_lbl.setText(f"Email: {email}")
        self.ui.welcome_lbl.setText(f"Welcome, {username}!")
        self.ui.verified_status_lbl.setText("Verification Status\n\n" + ("✅" if verified else "❌"))

        #api call to load user gallery
        result = self.api.get_user_gallery()

        if result.get("success"):
            images = result.get("images", [])
        else:
            print("Failed to fetch user gallery:", result.get("message"))
            images = []

        #likes count
        total_likes = sum(img.get("likes", 0) for img in images)

        #other stats count that shows up in profile page
        self.ui.img_count_lbl.setText(f"Total Uploaded\nimages\n\n {len(images)}")
        self.ui.img_count_lbl.setText(
            f"Total Uploaded images<br><br><span style='font-size:20px; font-weight:bold;'>{len(images)}</span>")
        self.ui.like_count_lbl.setText(f"Total likes\n\n {total_likes}")
        self.ui.like_count_lbl.setText(
            f"Total Likes<br><br><span style='font-size:20px; font-weight:bold;'>{total_likes}</span>")

        self.refresh_gallery()
    



