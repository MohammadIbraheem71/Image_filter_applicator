# pages/profile_auth_page.py
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from ui_py.profile_auth_page import Ui_profile_auth_page
from pages.dialog_boxes.login_dialog import login_dialog
from pages.dialog_boxes.signup_dialog import signup_dialog
from backend_api.client_api import client_api


#this contains the stuff regarding the auth page in the profile window
class profile_auth_page(QWidget):
    login_success = Signal(str)
    signup_success = Signal(str)

    def __init__(self, api_client: client_api):
        super().__init__()

        self.api = api_client

        self.ui = Ui_profile_auth_page()
        self.ui.setupUi(self)

        #button connections here
        self.ui.log_in_btn.clicked.connect(self.open_login_dialog)
        self.ui.sign_up_btn.clicked.connect(self.open_signup_dialog)

    def open_login_dialog(self):
        dlg = login_dialog(self.api, parent=self)
        dlg.login_success.connect(self.login_success.emit)
        dlg.exec()

    def open_signup_dialog(self):
        dlg = signup_dialog(self.api, parent=self)
        dlg.signup_success.connect(self.signup_success.emit)
        dlg.exec()
