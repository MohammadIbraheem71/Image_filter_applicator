# pages/dialog_boxes/request_reset_dialog.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from backend_api.client_api import client_api
from pages.dialog_boxes.resetpass_dialog import resetpass_dialog

class resetreq_dialog(QDialog):
    def __init__(self, api: client_api, parent=None):
        super().__init__(parent)
        self.api = api
        self.setWindowTitle("Request Password Reset")
        self.setFixedSize(400, 150)

        layout = QVBoxLayout(self)

        self.email_lbl = QLabel("Enter your email to reset password:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.request_btn = QPushButton("Request Reset Email")
        self.request_btn.clicked.connect(self.request_reset)

        layout.addWidget(self.email_lbl)
        layout.addWidget(self.email_input)
        layout.addWidget(self.request_btn)

    def request_reset(self):
        email = self.email_input.text().strip()
        if not email:
            QMessageBox.warning(self, "Error", "Please enter your email")
            return

        try:
            self.api.request_password_reset(email)
            QMessageBox.information(
                self, "Email Sent",
                "Reset email sent! Check your inbox for the token link."
            )
            # Open actual reset password dialog
            reset_dlg = resetpass_dialog(self.api, parent=self)
            reset_dlg.exec()
            self.accept()  # Close the request dialog
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to request reset: {e}")
