# dialogs/signup_dialog.py
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal
from ui_py.signup_dialog import Ui_signup_dialog
from backend_api.client_api import client_api

class signup_dialog(QDialog):

    signup_success = Signal(str)  # emits email

    def __init__(self, api_client: client_api, parent=None):
        super().__init__(parent)
        self.ui = Ui_signup_dialog()
        self.ui.setupUi(self)
        self.api = api_client

        # Connect QDialogButtonBox signals
        self.ui.signup_btn.clicked.connect(self._on_signup)  # OK button


    def _on_signup(self):
        username = self.ui.username_edt.text().strip()
        email = self.ui.email_edt.text().strip()
        password = self.ui.pswrd_edt.text().strip()

        if not email or not password or not username:
            QMessageBox.warning(self, "Missing Information", "Please enter username, email and password.")
            return

        # Call backend signup (returns True/False)
        try:
            success, error_msg = self.api.signup(username=username, email=email, password=password)
        except Exception as e:
            QMessageBox.critical(self, "Network Error", f"{e}")
            return

        if success:
            QMessageBox.information(self, "Verify Email", "Signup successful! Please check your email to verify your account.")
            self.accept()  # Close dialog   
        else:
            QMessageBox.warning(self, "Signup Failed", f"{error_msg}")