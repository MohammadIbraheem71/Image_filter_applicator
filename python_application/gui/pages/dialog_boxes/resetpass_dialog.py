# pages/dialog_boxes/reset_password_dialog.py
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
)
from PySide6.QtCore import Qt
from backend_api.client_api import client_api

class resetpass_dialog(QDialog):
    def __init__(self, api: client_api, parent=None):
        super().__init__(parent)
        self.api = api
        self.setWindowTitle("Reset Password")
        self.setFixedSize(400, 320)

        self.setStyleSheet("""
            QWidget#form_widget {
                background-color: rgba(220, 220, 220, 0.7);
                border: 1px solid rgba(200, 200, 200, 0.5);
                border-radius: 0px;
                padding: 20px;
            }
            QWidget#form_widget QLabel {
                background: transparent;
                color: #2D2440;
                font-weight: 500;
                padding: 0;
                border: none;
            }
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.25);
                border: 1px solid rgba(255, 255, 255, 0.4);
                border-radius: 8px;
                padding: 10px;
                color: #2D2440;
                font-size: 14px;
            }
            QLineEdit:focus {
                background-color: rgba(255, 255, 255, 0.35);
                border: 1px solid rgba(220, 180, 230, 0.8);
            }
            QPushButton#login_btn {
                background-color: #A855F7; 
                color: #FFFFFF;
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                font-weight: 700;
                font-size: 16px;
            }
            QPushButton#login_btn:hover {
                background-color: #C084FC;
            }
            QPushButton#login_btn:pressed {
                background-color: #9333EA;
                transform: scale(0.97);
            }
        """)

        # Form widget
        self.form_widget = QWidget(self)
        self.form_widget.setObjectName("form_widget")


        # - - SETTING UP WIDGTS AND LAYOUT - -
        layout = QVBoxLayout(self.form_widget)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignCenter)
        self.form_widget.setGeometry(0, 0, 400, 320)

        self.token_lbl = QLabel("Enter the token sent to your email:")
        self.token_input = QLineEdit()
        self.token_input.setPlaceholderText("Reset token")

        self.new_password_lbl = QLabel("Enter your new password:")
        self.new_password_input = QLineEdit()
        self.new_password_input.setPlaceholderText("New password")
        self.new_password_input.setEchoMode(QLineEdit.Password)

        self.reset_btn = QPushButton("Set New Password")
        self.reset_btn.setObjectName("login_btn")
        self.reset_btn.clicked.connect(self.reset_password)

        self.msg_lbl = QLabel("")
        self.msg_lbl.setWordWrap(True)
        self.msg_lbl.setVisible(False)

        self.token_input.textChanged.connect(lambda: self.msg_lbl.setVisible(False))
        self.new_password_input.textChanged.connect(lambda: self.msg_lbl.setVisible(False))


        layout.addWidget(self.token_lbl)
        layout.addWidget(self.token_input)
        layout.addWidget(self.new_password_lbl)
        layout.addWidget(self.new_password_input)
        layout.addWidget(self.msg_lbl)
        layout.addWidget(self.reset_btn)


    #functions for the errors and success msgss
    def show_error(self, text):
        self.msg_lbl.setText(text)
        self.msg_lbl.setStyleSheet("""
            background-color: rgba(248, 215, 218, 150);
            color: rgb(196, 62, 57);
            border: 1px solid rgba(196, 62, 57, 200);
            border-radius: 6px;
            padding: 6px 8px;
            font-weight: 500;
        """)
        self.msg_lbl.setVisible(True)

    def show_success(self, text):
        self.msg_lbl.setText(text)
        self.msg_lbl.setStyleSheet("""
            background-color: rgba(198, 239, 206, 150);
            color: rgb(0, 97, 0);
            border: 1px solid rgba(0, 97, 0, 200);
            border-radius: 6px;
            padding: 6px 8px;
            font-weight: 500;
        """)
        self.msg_lbl.setVisible(True)

    def reset_password(self):
        token = self.token_input.text().strip()
        new_password = self.new_password_input.text().strip()

        if not token or not new_password:
            self.show_error("Token and new password are required.")
            return

        try:
            self.api.reset_password(token, new_password)
            self.show_success("Password reset successfully!")
        except Exception as e:
            msg = str(e).lower()

            if "connection" in msg or "failed to establish" in msg or "max retries" in msg:
                self.show_error("Cannot reach server. Please try again later.")
                return
            elif  "404 client error" in msg:
                self.show_error("Incorrect token")
                return
            else:
                # Show actual backend message for real errors (email wrong etc.)
                self.show_error(f"{e}")
