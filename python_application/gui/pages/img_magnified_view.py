#this is the img_magnified_view widget. supposed to open the image in a larger view

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from ui_py.img_magnified_view import Ui_img_magnified_view
import requests
from io import BytesIO
from PIL import Image


#this class handles the like and unlike logic as well, similar to how the image widget handled it
class img_magnified_view_widget(QWidget):
    def __init__(self, api=None, image_url=None, image_id=None,
                 uploaded_by="", uploaded_at="", description="",
                 likes=0, liked_by_user=False):

        super().__init__()
        self.ui = Ui_img_magnified_view()
        self.ui.setupUi(self)

        self.api = api
        self.image_url = image_url
        self.image_id = image_id
        self.likes = likes
        self.liked_by_user = liked_by_user

        #we fill out the labels here 
        self.ui.uploaded_by_lbl.setText(f"Uploaded by: {uploaded_by}")
        self.ui.uploaded_at_lbl.setText(f"Uploaded at: {uploaded_at}")
        self.ui.description_lbl.setText(description)
        self.ui.like_counter_lbl.setText(str(self.likes))

        #if a url is provided we load the image
        if self.image_url:
            self.load_image(self.image_url)

        #similar to the image widget class
        self._update_like_button_state()


        self.ui.like_btn.clicked.connect(self.toggle_like)
        self.ui.liked_btn.clicked.connect(self.toggle_like)


    #this function loads the image,might need some tinkering
    #NEED TO MAKE THIS NON BLOCKING MULTI THREADING
    def load_image(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()

            pil_img = Image.open(BytesIO(response.content)).convert("RGBA")
            qimg = QImage(
                pil_img.tobytes("raw", "RGBA"),
                pil_img.width,
                pil_img.height,
                QImage.Format_RGBA8888,
            )
            pixmap = QPixmap.fromImage(qimg)

            self.ui.image_lbl.setPixmap(pixmap.scaled(
                self.ui.image_lbl.width(),
                self.ui.image_lbl.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            ))

        except Exception as e:
            print(f"Failed to load magnified image: {e}")
            self.ui.image_lbl.setText("Failed to load image")

    #this manages the like state of the button
    def _update_like_button_state(self):
        if not self.api or not self.api.token:
            # Guest user → disable like buttons
            self.ui.like_btn.setEnabled(False)
            self.ui.liked_btn.setEnabled(False)
            return

        if self.liked_by_user:
            self.ui.like_btn.setVisible(False)
            self.ui.liked_btn.setVisible(True)
        else:
            self.ui.like_btn.setVisible(True)
            self.ui.liked_btn.setVisible(False)


    def toggle_like(self):
        if not self.api or not self.image_id:
            print("Missing API or image_id")
            return

        try:
            #like logic here
            if self.ui.like_btn.isVisible():
                res = self.api.like_image(self.image_id)
                if res.get("success"):
                    self.likes += 1
                    self.liked_by_user = True
                    self.ui.like_btn.setVisible(False)
                    self.ui.liked_btn.setVisible(True)

            #unlike logic here
            else:
                res = self.api.unlike_image(self.image_id)
                if res.get("success"):
                    self.likes -= 1
                    self.liked_by_user = False
                    self.ui.like_btn.setVisible(True)
                    self.ui.liked_btn.setVisible(False)

            self.ui.like_counter_lbl.setText(str(self.likes))

        except Exception as e:
            print("Error toggling like:", e)
