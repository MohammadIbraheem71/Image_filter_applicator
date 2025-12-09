# pages/dialog_boxes/request_reset_dialog.py
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
)
from PySide6.QtCore import Qt
from backend_api.client_api import client_api
from pages.dialog_boxes.resetpass_dialog import resetpass_dialog

class resetreq_dialog(QDialog):
    def __init__(self, api: client_api, parent=None):
        super().__init__(parent)
        self.api = api
        self.setWindowTitle("Request Password Reset")
        self.setFixedSize(400, 240)

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

        # Main form
        self.form_widget = QWidget(self)
        self.form_widget.setObjectName("form_widget")
        self.form_widget.setGeometry(0, 0, self.width(), self.height())

        layout = QVBoxLayout(self.form_widget)
        layout.setSpacing(12)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignCenter)

        # Fields
        self.email_lbl = QLabel("Enter your email to reset password:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.request_btn = QPushButton("Request Reset Email")
        self.request_btn.setObjectName("login_btn")
        self.request_btn.clicked.connect(self.request_reset)

        # Inline message label
        self.msg_lbl = QLabel("")
        self.msg_lbl.setWordWrap(True)
        self.msg_lbl.setVisible(False)

        layout.addWidget(self.email_lbl)
        layout.addWidget(self.email_input)
        layout.addWidget(self.msg_lbl)
        layout.addWidget(self.request_btn)

        self.email_input.textChanged.connect(lambda: self.msg_lbl.setVisible(False))
   

   #functions for success and errors messegs
    def show_error(self, text):
        self.msg_lbl.setText(text)
        self.msg_lbl.setStyleSheet("""
            background-color: rgba(248, 215, 218, 150);
            color: rgb(196, 62, 57);
            border: 1px solid rgba(196, 62, 57, 200);
            border-radius: 4px;
            padding: 4px 6px;
        """)
        self.msg_lbl.setVisible(True)

    def show_success(self, text):
        self.msg_lbl.setText(text)
        self.msg_lbl.setStyleSheet("""
            background-color: rgba(198, 239, 206, 150);
            color: rgb(0, 97, 0);
            border: 1px solid rgba(0, 97, 0, 200);
            border-radius: 4px;
            padding: 4px 6px;
        """)
        self.msg_lbl.setVisible(True)

    def request_reset(self):
        email = self.email_input.text().strip()

        if not email:
            self.show_error("Please enter your email.")
            return

        try:
            self.api.request_password_reset(email)

            self.show_success("Reset email sent! Check your inbox.")

            # Open token entry dialog
            reset_dlg = resetpass_dialog(self.api, parent=self)
            reset_dlg.exec()

            self.accept()
        except Exception as e:
            msg = str(e).lower()

            if "connection" in msg or "failed to establish" in msg or "max retries" in msg:
                self.show_error("Cannot reach server. Please try again later.")
                return
            elif  "not found" in msg:
                self.show_error("Email not registered in system.")
                return
            else:
                # Show actual backend message for real errors (email wrong etc.)
                self.show_error(f"{e}")
