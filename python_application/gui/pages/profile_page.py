from PySide6.QtWidgets import QWidget, QStackedWidget
from pages.profile_auth_page import profile_auth_page
from pages.profile_logged_page import profile_logged_page
from backend_api.client_api import client_api

class profile_page:
    def __init__(self, page_widget, api_client):
        self.ui = page_widget
        self.api = api_client

        # Keep references to stacked widget and child pages
        self.profile_windows: QStackedWidget = self.ui.findChild(QStackedWidget, "profile_windows")
        self.auth_page_widget: QWidget = self.ui.findChild(QWidget, "auth_page")
        self.logged_page_widget: QWidget = self.ui.findChild(QWidget, "logged_page")

        # Initialize page logic objects and keep them alive
        self.auth_page = profile_auth_page(self.auth_page_widget, self.api)
        self.logged_page = profile_logged_page(self.logged_page_widget)

        # Make sure the signal uses the stored widget reference
        self.auth_page.login_sucess.connect(self.show_logged_page)
        
    def show_logged_page(self):
        """Switch to the logged page safely."""
        if self.logged_page_widget is not None and self.profile_windows is not None:
            self.profile_windows.setCurrentWidget(self.logged_page_widget)