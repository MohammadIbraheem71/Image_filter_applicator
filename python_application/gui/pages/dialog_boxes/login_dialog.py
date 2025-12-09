# dialogs/login_dialog.py
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon
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

        # hide the error labels at the start
        self.ui.error_lbl.setVisible(False)
        self.ui.success_lbl.setVisible(False)

        #connecting buttons to respectiv funcs
        self.ui.login_btn.clicked.connect(self._on_submit)
        self.ui.forgotpass_btn.clicked.connect(self.open_reset_password_dialog)

        #when typing, clear any success, error msgs 
        self.ui.email_edt.textChanged.connect(self.clear_labels)
        self.ui.passwrd_edt.textChanged.connect(self.clear_labels)

        # ---------------- Password visibility button ----------------
        self.show_pass_btn = QPushButton(self.ui.passwrd_edt)
        self.show_pass_btn.setCursor(Qt.PointingHandCursor)
        self.show_pass_btn.setFlat(True)
        self.show_pass_btn.setStyleSheet("background: transparent; border: none;")
        self.show_pass_btn.setFixedSize(40,16)

        self.eye_icon = QIcon(":/icons/assets/eye.png")
        self.eye_hide_icon = QIcon(":/icons/assets/hidden_eye.png")
        self.show_pass_btn.setIcon(self.eye_hide_icon)
        self.show_pass_btn.setIconSize(self.show_pass_btn.size())

        self.password_visible = False
        self.ui.passwrd_edt.setEchoMode(QLineEdit.Password)
        self.show_pass_btn.clicked.connect(self.toggle_password)

        # Position button
        self._position_password_button()
        self.ui.passwrd_edt.resizeEvent = lambda event: self._position_password_button()
        self.ui.passwrd_edt.setStyleSheet("padding-right: 10px;")

    #helper methods
    def show_error(self, message: str):
        self.ui.error_lbl.setText(message)
        self.ui.error_lbl.setVisible(True)
        self.ui.success_lbl.setVisible(False)

    def show_success(self, message: str):
        self.ui.success_lbl.setText(message)
        self.ui.success_lbl.setVisible(True)
        self.ui.error_lbl.setVisible(False)

    def clear_labels(self):
        """Hide both error and success labels."""
        self.ui.error_lbl.setVisible(False)
        self.ui.error_lbl.setText("")
        self.ui.success_lbl.setVisible(False)
        self.ui.success_lbl.setText("")

    def toggle_password(self):
        self.password_visible = not self.password_visible
        if self.password_visible:
            self.ui.passwrd_edt.setEchoMode(QLineEdit.Normal)
            self.show_pass_btn.setIcon(self.eye_icon)
        else:
            self.ui.passwrd_edt.setEchoMode(QLineEdit.Password)
            self.show_pass_btn.setIcon(self.eye_hide_icon)

    def _position_password_button(self):
        self.show_pass_btn.move(
            self.ui.passwrd_edt.rect().right() - self.show_pass_btn.width() - 5,
            (self.ui.passwrd_edt.rect().height() - self.show_pass_btn.height()) // 2
        )

    
    def _on_submit(self):
        # Clear previous messages
        self.clear_labels()

        email = self.ui.email_edt.text().strip()
        password = self.ui.passwrd_edt.text().strip()

        if not email and not password:
            self.show_error("Enter email and password.")
            return
        elif not email:
            self.show_error("Enter email.")
            return
        elif not password:
            self.show_error("Enter password.")
            return

        try:
            result = self.api.login(email=email, password=password)
        except Exception:
            self.show_error("Network error. Try again.")
            return

        if result == "unverified":
            self.show_error("Please verify your email before logging in.")
            return

        if not result:
            self.show_error("Incorrect email or password.")
            return

        # SUCCESS
        self.show_success("Login successful!")
        self.login_success.emit(email)
       

    def open_reset_password_dialog(self):
        from pages.dialog_boxes.resetreq_dialog import resetreq_dialog
        dlg = resetreq_dialog(self.api, parent=self)
        dlg.exec()
