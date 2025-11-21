from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Signal

class profile_auth_page(QWidget):
    login_sucess = Signal()
    
    def __init__(self, page_widget, api_client):
        super().__init__()
        self.page = page_widget
        self.api = api_client
        
        self.login_btn = self.page.findChild(QPushButton, "login_btn")
        self.signup_btn = self.page.findChild(QPushButton, "signup_btn")
        
        self.login_btn.clicked.connect(self.handle_login)
        self.signup_btn.clicked.connect(self.handle_signup)
        
    def handle_login(self):
        print("user logging in")
        
    def handle_signup(self):
        print("user signing up")