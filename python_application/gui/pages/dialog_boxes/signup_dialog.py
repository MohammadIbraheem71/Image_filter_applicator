# dialogs/signup_dialog.py
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon
from ui_py.signup_dialog import Ui_signup_dialog
from backend_api.client_api import client_api

class signup_dialog(QDialog):
    """Modal signup dialog."""

    signup_success = Signal(str)  # emits email

    def __init__(self, api_client: client_api, parent=None):
        super().__init__(parent)
        self.ui = Ui_signup_dialog()
        self.ui.setupUi(self)
        self.api = api_client

        # Initially hide error label
        self.ui.error_lbl.setVisible(False)
        self.ui.success_lbl.setVisible(False)

        # Connect buttons
        self.ui.signup_btn.clicked.connect(self._on_signup)

        # Clear error when typing
        self.ui.username_edt.textChanged.connect(self.clear_labels)
        self.ui.email_edt.textChanged.connect(self.clear_labels)
        self.ui.passwrd_edt.textChanged.connect(self.clear_labels)
        self.ui.crm_passwrd_edt.textChanged.connect(self.clear_labels)

        # ---------------- Password visibility buttons ----------------
        self.eye_icon = QIcon("assets/eye.png")
        self.eye_hide_icon = QIcon("assets/eye_hide.png")

        # Main password field button
        self.show_pass_btn = QPushButton(self.ui.passwrd_edt)
        self._setup_eye_button(self.show_pass_btn, self.ui.passwrd_edt)
        self.show_pass_btn.clicked.connect(lambda: self.toggle_password(self.ui.passwrd_edt, self.show_pass_btn))

        # Confirm password field button (crm_passwrd_edt)
        self.show_crm_pass_btn = QPushButton(self.ui.crm_passwrd_edt)
        self._setup_eye_button(self.show_crm_pass_btn, self.ui.crm_passwrd_edt)
        self.show_crm_pass_btn.clicked.connect(lambda: self.toggle_password(self.ui.crm_passwrd_edt, self.show_crm_pass_btn))

    # ---------------- Helper methods ----------------
    def _setup_eye_button(self, button: QPushButton, line_edit: QLineEdit):
        """Configure eye button inside a QLineEdit."""
        button.setCursor(Qt.PointingHandCursor)
        button.setFlat(True)
        button.setStyleSheet("background: transparent; border: none;")
        button.setFixedSize(40,16)
        button.setIcon(self.eye_icon)
        button.setIconSize(button.size())
        line_edit.setEchoMode(QLineEdit.Password)
        line_edit.setStyleSheet("padding-right: 10px;")
        # Position button and update on resize
        button.move(line_edit.rect().right() - button.width() - 5,
                    (line_edit.rect().height() - button.height()) // 2)
        line_edit.resizeEvent = lambda event, b=button, le=line_edit: self._position_password_button(le, b)

    def _position_password_button(self, line_edit: QLineEdit, button: QPushButton):
        """Position the eye button inside the QLineEdit."""
        button.move(
            line_edit.rect().right() - button.width() - 5,
            (line_edit.rect().height() - button.height()) // 2
        )

    def toggle_password(self, line_edit: QLineEdit, button: QPushButton):
        """Toggle password visibility and icon for a specific field."""
        if line_edit.echoMode() == QLineEdit.Password:
            line_edit.setEchoMode(QLineEdit.Normal)
            button.setIcon(self.eye_icon)
        else:
            line_edit.setEchoMode(QLineEdit.Password)
            button.setIcon(self.eye_hide_icon)

    def show_error(self, message: str):
        """Display error inline and make label visible."""
        self.ui.error_lbl.setText(message)
        self.ui.error_lbl.setVisible(True)

    def clear_labels(self):
        """Hide both error and success labels."""
        self.ui.error_lbl.setVisible(False)
        self.ui.error_lbl.setText("")
        self.ui.success_lbl.setVisible(False)
        self.ui.success_lbl.setText("")

    def show_success(self, message: str):
        """Display success label."""
        self.ui.success_lbl.setText(message)
        self.ui.success_lbl.setVisible(True)
        self.ui.error_lbl.setVisible(False)


    # ---------------- Signup logic ----------------
    def _on_signup(self):
        username = self.ui.username_edt.text().strip()
        email = self.ui.email_edt.text().strip()
        password = self.ui.passwrd_edt.text().strip()
        confirm_password = self.ui.crm_passwrd_edt.text().strip()
        self.ui.success_lbl.setVisible(False)
        self.ui.success_lbl.setText("")

        # INPUT VALIDATION
        if not username:
            self.show_error("Username is required")
            return
        if not email:
            self.show_error("Email is required")
            return
        if not password:
            self.show_error("Password is required")
            return
        if password != confirm_password:
            self.show_error("Passwords do not match")
            return

        # API CALL
        try:
            success, error_msg = self.api.signup(username=username, email=email, password=password)
        except Exception as e:
            self.show_error(f"Network error: {e}")
            return

        # SUCCESS
        if success:
            self.show_success("Signup successful! Please check your email to verify your account.")
            self.signup_success.emit(email)
        else:
            self.show_error(error_msg)
