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
        
        # Buttons
        self.ui.logout_btn.clicked.connect(self.logout)

        self.delete_listner = event_listner(event_name="request_delete", callback=self.delete_image)

        # Auto-refresh on events
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
            
            # Get or create layout
            layout = self.ui.image_grid.layout()
            if layout is None:
                from PySide6.QtWidgets import QGridLayout
                layout = QGridLayout(self.ui.image_grid)
                self.ui.image_grid.setLayout(layout)

            # Clear existing widgets (images or previous message)
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.setParent(None)

            if images_list:
                # Load images only if list is not empty
                self.loader.load_images(images=images_list)
            else:
                # Show empty message if truly empty
                self.show_empty_gallery_message()
            
        except Exception as e:
            print("Error fetching gallery:", e)

    def show_empty_gallery_message(self):
        # Create message label
       
        msg = QLabel("You have not uploaded any images yet.", self.ui.image_grid)
        msg.setStyleSheet("""
            QLabel {
                font-size: 18px;
                color: white;
                padding: 20px;
                background: transparent;
            }
        """)
        msg.setAlignment(Qt.AlignCenter)

        # Put label in the grid area
        container = QWidget()
        v = QVBoxLayout(container)
        v.addWidget(msg)
        v.setAlignment(Qt.AlignCenter)

        self.ui.image_grid.layout().addWidget(container)


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
        self.ui.verified_status_lbl.setText("Verification Status\n\n" + ("✅" if verified else "❌"))

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
        self.ui.img_count_lbl.setText(f"Total Uploaded\nimages\n\n {len(images)}")
        self.ui.img_count_lbl.setText(
            f"Total Uploaded images<br><br><span style='font-size:20px; font-weight:bold;'>{len(images)}</span>")
        self.ui.like_count_lbl.setText(f"Total likes\n\n {total_likes}")
        self.ui.like_count_lbl.setText(
            f"Total Likes<br><br><span style='font-size:20px; font-weight:bold;'>{total_likes}</span>")

        self.refresh_gallery()
    



