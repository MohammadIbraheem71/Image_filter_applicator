from PySide6.QtWidgets import QWidget, QStackedWidget
from ui_py.profile_page import Ui_profile_pg
from backend_api.client_api import client_api
from pages.profile_auth_page import profile_auth_page
from pages.profile_logged_page import profile_logged_page

class profile_page(QWidget):
    def __init__(self, api_client):
        super().__init__()
        # Set up UI
        self.ui = Ui_profile_pg()
        self.ui.setupUi(self)
        self.api = api_client

        # Reference stacked widget and its pages
        self.profile_windows: QStackedWidget = self.ui.profile_windows
        self.auth_page_widget: QWidget = self.ui.auth_page
        self.logged_page_widget: QWidget = self.ui.logged_page

        # Initialize logic pages
        self.auth_page = profile_auth_page(self.auth_page_widget, self.api)
        self.logged_page = profile_logged_page(self.logged_page_widget)

        # Connect login signal to switch page
        self.auth_page.login_sucess.connect(self.show_logged_page)

    def show_logged_page(self):
        """Switch to the logged-in page safely."""
        self.profile_windows.setCurrentWidget(self.logged_page_widget)
