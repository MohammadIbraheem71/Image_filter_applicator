# pages/profile_page.py
from PySide6.QtWidgets import QWidget, QStackedWidget
from PySide6.QtCore import Signal
from ui_py.profile_page import Ui_profile_pg
from pages.dialog_boxes.login_dialog import login_dialog
from pages.dialog_boxes.signup_dialog import signup_dialog
from pages.profile_logged_page import profile_logged_page
from backend_api.client_api import client_api


class profile_page(QWidget):
    """Profile page container with login/signup dialogs and logged-in view."""

    # Optional: emit when user logs in successfully
    user_logged_in = Signal(str)

    def __init__(self, api_client: client_api):
        super().__init__()

        # Setup UI
        self.ui = Ui_profile_pg()
        self.ui.setupUi(self)
        self.api = api_client

        # Reference stacked widget and pages
        self.profile_windows: QStackedWidget = self.ui.profile_windows
        self.auth_page_widget: QWidget = self.ui.auth_pg
        self.logged_page_widget: QWidget = self.ui.logged_pg

        # Initialize the logged page logic
        self.logged_page = profile_logged_page(self.logged_page_widget)

        # Connect buttons in auth_page_widget to open dialogs
        self.ui.log_in_btn.clicked.connect(self.open_login_dialog)
        self.ui.sign_up_btn.clicked.connect(self.open_signup_dialog)

        #if no token is found then we set the current page to be the auth page, as user
        #needs to log in or sign up
        if self.api.token == None:
            self.profile_windows.setCurrentWidget(self.auth_page_widget)

   
    #open the login dialog
    def open_login_dialog(self):
        login_dlg = login_dialog(self.api, parent=self)
        login_dlg.login_success.connect(self.on_login_success)
        login_dlg.exec()  # modal

    #open the sign up dialog
    def open_signup_dialog(self):
        signup_dlg = signup_dialog(self.api, parent=self)
        signup_dlg.signup_success.connect(lambda user: print(f"Signup complete for {user}"))
        signup_dlg.exec()  # modal

    # -------------------- Handlers --------------------

    def on_login_success(self, user):
        """Handle successful login."""
        # Switch stacked widget to logged page
        self.profile_windows.setCurrentWidget(self.logged_page_widget)

        #we need to update the logged page to reflect the user's information
        #self.logged_page.update_user_info(user)

        # Emit signal for MainWindow or other pages
        self.user_logged_in.emit(user)
