# pages/profile_page.py
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from ui_py.profile_page import Ui_profile_pg
from pages.profile_auth_page import profile_auth_page
from pages.profile_logged_page import profile_logged_page

from backend_api.client_api import client_api


#this is the main profile page, contains only a stacked widget. loads the auth page and logged page and switches between them
class profile_page(QWidget):

    user_logged_in = Signal(str)

    def __init__(self, api_client: client_api):
        super().__init__()

        self.api = api_client

        # Load container UI
        self.ui = Ui_profile_pg()
        self.ui.setupUi(self)

        #the stacked widget inside the container
        self.profile_windows = self.ui.profile_windows

        #ccreate the two pages
        self.auth_page = profile_auth_page(self.api)
        self.logged_page = profile_logged_page(self.api)

        #add widgets to the stacked widget
        self.profile_windows.addWidget(self.auth_page)
        self.profile_windows.addWidget(self.logged_page)

        #connecting signals
        self.auth_page.login_success.connect(self.on_login_success)
        self.auth_page.signup_success.connect(self.on_signup_success)

        self.logged_page.logout_requested.connect(self.on_logout)

        # If the user is not logged in → show auth page
        if self.api.token is None:
            self.profile_windows.setCurrentWidget(self.auth_page)
        else:
            self.profile_windows.setCurrentWidget(self.logged_page)
            self.logged_page.refresh_user_page()


    def refresh_gallery(self):
        if self.api.token != None:
            self.logged_page.refresh_gallery()

    def on_login_success(self, email):
        """Switch to logged page."""
        self.profile_windows.setCurrentWidget(self.logged_page)
        self.logged_page.refresh_user_page()
        self.user_logged_in.emit(email)

    def on_signup_success(self, email):
        print("Signup completed for:", email)

    def on_logout(self):
        """Switch back to auth page."""
        self.api.token = None
        self.api.user_info = None
        self.profile_windows.setCurrentWidget(self.auth_page)
