import requests
import mimetypes
import os
from PySide6.QtCore import QObject, Signal


class AuthAPI:
    def __init__(self, base_url, http_client=requests):
        self.base_url = base_url
        self.token = None
        self.user_info = None
        self.http_client = http_client

    def login(self, email, password):
        url = f"{self.base_url}/routes/auth/login"
        response = self.http_client.post(url, json={"email": email, "password": password})
        if response.status_code == 200:
            data = response.json()
            self.token = data["token"]
            self.user_info = data["user"]
            print("User logged in successfully")
            return True
        else:
            data = response.json()
            error_msg = data.get("error", "")
            if "verify your email" in error_msg.lower():
                print("Email not verified")
                return "unverified"
            else:
                print("Invalid credentials")
                return False

    def signup(self, username, email, password):
        url = f"{self.base_url}/routes/auth/signup"
        try:
            response = self.http_client.post(url, json={"username": username, "email": email, "password": password})
            if response.status_code == 201:
                print(f"User '{email}' signed up successfully")
                return True, None
            else:
                try:
                    data = response.json()
                    error_msg = data.get("error", "Unknown error")
                except Exception:
                    error_msg = response.text or "Unknown error"
                print(f"Signup failed: {error_msg}")
                return False, error_msg
        except self.http_client.RequestException as e:
            print(f"Network error: {e}")
            return False, str(e)

    def request_password_reset(self, email):
        url = f"{self.base_url}/routes/auth/reset-password-request"
        resp = self.http_client.post(url, json={"email": email})
        resp.raise_for_status()
        return resp.json()

    def reset_password(self, token, new_password):
        url = f"{self.base_url}/routes/auth/reset-password"
        resp = self.http_client.post(url, json={"token": token, "newPassword": new_password})
        resp.raise_for_status()
        return resp.json()
