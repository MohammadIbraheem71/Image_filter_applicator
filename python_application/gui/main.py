# main.py
import sys
import os

# Add the parent folder (python_application) to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QMovie, QIcon   
from PySide6.QtCore import QSize

from ui_py.app_gui import Ui_MainWindow
from filters.filter_factory import filter_factory
from filters.filter_types.blur_filter import blur_filter
from filters.filter_types.sepia_filter import sepia_filter
from filters.filter_types.edge_filter import edge_filter
from filters.filter_types.grayscale_filter import grayscale_filter
from image_handler.image_handler import image_handler

from pages.filter_page import FilterPage
from pages.gallery_page import gallery_page
from pages.profile_page import profile_page

from backend_api.client_api import client_api

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.api = client_api("http://localhost:3000")
        
        gif_path = os.path.join(BASE_DIR, "gui", "assets", "logo.gif")
        # Example path → change it if your GIF is elsewhere

        if os.path.exists(gif_path):
            self.movie = QMovie(gif_path)
            self.movie.setScaledSize(QSize(30, 30))
            self.ui.logo_gif.setMovie(self.movie)
            self.movie.start()
        else:
            print("⚠️ GIF not found at:", gif_path)
        
        # Shared objects
        self.factory = filter_factory()
        self.factory.add_filter("blur", blur_filter())
        self.factory.add_filter("edge", edge_filter())
        self.factory.add_filter("sepia", sepia_filter())
        self.factory.add_filter("grayscale", grayscale_filter())
        self.handler = image_handler()

        # Initialize pages
        self.filter_page = FilterPage(self.factory, self.handler)  # <-- new FilterPage
        self.gallery_page = gallery_page(self.api) 
        self.profile_page = profile_page(self.api)

        # Add filter_page to the main stacked widget
        self.ui.windows.addWidget(self.filter_page)
        self.ui.windows.addWidget(self.gallery_page)
        self.ui.windows.addWidget(self.profile_page)

        # Sidebar button navigation
        self.ui.filter_pg_btn.clicked.connect(
            lambda: self.ui.windows.setCurrentWidget(self.filter_page)
        )

        self.ui.gallery_pg_btn.clicked.connect(
            lambda: self.ui.windows.setCurrentWidget(self.gallery_page)
        )
        
        self.ui.profile_pg_btn.clicked.connect(
            lambda: self.ui.windows.setCurrentWidget(self.profile_page)
        )

        # Set initial page
        self.ui.windows.setCurrentWidget(self.filter_page)


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
