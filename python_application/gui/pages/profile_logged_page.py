# pages/profile_logged_page.py
import requests
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from ui_py.profile_logged_page import Ui_profile_logged_page
from backend_api.client_api import client_api

from utils.image_loader import image_loader
from pages.widgets.image_widget_trash import image_widget_trash
from utils.event_listner import event_listner


#this is the profile logged page
class profile_logged_page(QWidget):

    logout_requested = Signal()

    def __init__(self, api_client: client_api):
        super().__init__()

        self.api = api_client

        self.ui = Ui_profile_logged_page()
        self.ui.setupUi(self)

        self.loader = image_loader(self.ui.image_grid, columns=2, api=self.api, widget_cls=image_widget_trash)

        # Buttons
        self.ui.logout_btn.clicked.connect(self.logout)

        self.delete_listner = event_listner(event_name="request_delete", callback=self.delete_image)

        # Auto-refresh on events
        # self.api.image_uploaded.connect(self.refresh_user_page)
        # self.api.image_liked.connect(self.refresh_user_page)
        # self.api.image_unliked.connect(self.refresh_user_page)
        self.api.image_deleted.connect(self.refresh_gallery)
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
            self.loader.load_images(images=images_list)
        except Exception as e:
            print("Error fetching gallery:", e)

    #we handle the logout here
    def logout(self):
        self.logout_requested.emit()

    #we load the user info here
    def refresh_user_page(self):
        if not self.api.token:
            return

        # --- User Info ---
        email = self.api.user_info.get("email", "Unknown")
        username = self.api.user_info.get("username", "User")
        verified = self.api.user_info.get("is_verified", 0)

        self.ui.email_lbl.setText(f"Email: {email}")
        self.ui.welcome_lbl.setText(f"Welcome, {username}!")
        self.ui.verified_status_lbl.setText("Verification: " + ("✅" if verified else "❌"))

        # --- Load user gallery using API function ---
        result = self.api.get_user_gallery()

        if result.get("success"):
            images = result.get("images", [])
        else:
            print("Failed to fetch user gallery:", result.get("message"))
            images = []

        # Count likes
        total_likes = sum(img.get("likes", 0) for img in images)

        # --- Stats ---
        self.ui.img_count_lbl.setText(f"Uploaded images: {len(images)}")
        self.ui.like_count_lbl.setText(f"Total likes: {total_likes}")

        # --- Load images into the grid ---
        self.loader.load_images(images)



