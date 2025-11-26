# pages/dialog_boxes/reset_password_dialog.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from backend_api.client_api import client_api

class resetpass_dialog(QDialog):
    def __init__(self, api: client_api, parent=None):
        super().__init__(parent)
        self.api = api
        self.setWindowTitle("Reset Password")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout(self)

        self.token_lbl = QLabel("Enter the token from your email:")
        self.token_input = QLineEdit()
        self.token_input.setPlaceholderText("Reset token")

        self.new_password_lbl = QLabel("Enter new password:")
        self.new_password_input = QLineEdit()
        self.new_password_input.setPlaceholderText("New password")
        self.new_password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.reset_btn = QPushButton("Set New Password")
        self.reset_btn.clicked.connect(self.reset_password)

        layout.addWidget(self.token_lbl)
        layout.addWidget(self.token_input)
        layout.addWidget(self.new_password_lbl)
        layout.addWidget(self.new_password_input)
        layout.addWidget(self.reset_btn)

    def reset_password(self):
        token = self.token_input.text().strip()
        new_password = self.new_password_input.text().strip()
        if not token or not new_password:
            QMessageBox.warning(self, "Error", "Token and new password required")
            return

        try:
            self.api.reset_password(token, new_password)
            QMessageBox.information(self, "Success", "Password reset successfully!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to reset password: {e}")
