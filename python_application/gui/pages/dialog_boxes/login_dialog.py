# dialogs/login_dialog.py
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal
from ui_py.login_dialog import Ui_login_dialog
from backend_api.client_api import client_api

class login_dialog(QDialog):
    """Modal login dialog."""

    login_success = Signal(str)  # emits username/email

    def __init__(self, api_client: client_api, parent=None):
        super().__init__(parent)
        self.ui = Ui_login_dialog()
        self.ui.setupUi(self)
        self.api = api_client

        # Connect buttons
        self.ui.buttonBox.accepted.connect(self._on_submit)  # OK
        self.ui.buttonBox.rejected.connect(self.reject)      # Cancel
        self.ui.forgotpass_btn.clicked.connect(self.open_reset_password_dialog) #forgot password


    def _on_submit(self):
        email = self.ui.email_edt.text().strip()
        password = self.ui.pswrd_edt.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Missing", "Enter email and password.")
            return

        try:
            result = self.api.login(email=email, password=password)
        except Exception as e:
            QMessageBox.critical(self, "Network Error", f"{e}")
            return

        if result == "unverified":
            QMessageBox.warning(self, "Email Not Verified", "Please verify your email before logging in.")
            return
        elif not result:
            QMessageBox.warning(self, "Login failed", "Incorrect email or password.")
            return

        self.login_success.emit(email)

        self.accept()  # closes dialog

    def open_reset_password_dialog(self):
        from pages.dialog_boxes.resetreq_dialog import resetreq_dialog
        dlg = resetreq_dialog(self.api, parent=self)
        dlg.exec()