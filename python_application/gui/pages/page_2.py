#place holder file for now
# pages/page2.py
from PySide6.QtWidgets import QLabel, QVBoxLayout

class Page2:
    def __init__(self, page_widget):
        self.page = page_widget
        layout = QVBoxLayout()
        label = QLabel("This is Page 2 placeholder")
        layout.addWidget(label)
        self.page.setLayout(layout)
