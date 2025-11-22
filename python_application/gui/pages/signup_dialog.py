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
        self.ui.buttonBox.accepted.connect(self._on_signup)  # OK button
        self.ui.buttonBox.rejected.connect(self.reject)      # Cancel button

    def _on_signup(self):
        email = self.ui.email_edt.text().strip()
        password = self.ui.pswrd_edt.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Missing Information", "Please enter both email and password.")
            return

        # Call backend signup (returns True/False)
        try:
            success = self.api.signup(email=email, password=password)
        except Exception as e:
            QMessageBox.critical(self, "Network Error", f"{e}")
            return

        if success:
            QMessageBox.information(self, "Account Created", f"Signup successful for {email}.")
            self.signup_success.emit(email)
            self.accept()  # close dialog
        else:
            QMessageBox.warning(self, "Signup Failed", "Could not create account. Please try again.")
