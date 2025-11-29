from PySide6.QtCore import QObject, Signal
from backend_api.AuthAPI import AuthAPI
from backend_api.GalleryAPI import GalleryAPI

#SRP fixed
#AuthAPI handles *only* authentication and GalleryAPI handles *only* gallery/image operations
#DIP fixed
#client_api depends on higher-level abstractions (AuthAPI, GalleryAPI) instead of concrete request logic.


class client_api(QObject):
    image_uploaded = Signal()

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

        # Separate concerns
        self.auth = AuthAPI(base_url)
        self.gallery = GalleryAPI(base_url)

        # Connect signals
        self.gallery.image_uploaded.connect(self.image_uploaded.emit)

    # ----------- token property for backward compatibility -----------
    @property
    def token(self):
        return self.auth.token

    @token.setter
    def token(self, value):
        self.auth.token = value
        self.gallery.token = value  # keep gallery in sync
    
    # user_info passthrough
    @property
    def user_info(self):
        return self.auth.user_info
    
    @user_info.setter
    def user_info(self, value):
        self.auth.user_info = value

    # ---------- Auth methods ----------
    def login(self, email, password):
        result = self.auth.login(email, password)
        if result is True:
            # pass token to gallery after login
            self.gallery.token = self.auth.token
        return result

    def signup(self, username, email, password):
        return self.auth.signup(username, email, password)

    def request_password_reset(self, email):
        return self.auth.request_password_reset(email)

    def reset_password(self, token, new_password):
        return self.auth.reset_password(token, new_password)

    # ---------- Gallery methods ----------
    def get_gallery(self):
        return self.gallery.get_gallery()

    def upload_image(self, file_path, filename):
        return self.gallery.upload_image(file_path, filename)
