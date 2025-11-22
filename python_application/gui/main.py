# main.py
import sys
import os

# Add the parent folder (python_application) to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from PySide6.QtWidgets import QApplication, QMainWindow
from python_application.gui.ui_py.app_gui import Ui_MainWindow
from filters.filter_factory import filter_factory
from filters.filter_types.blur_filter import blur_filter
from filters.filter_types.sepia_filter import sepia_filter
from filters.filter_types.edge_filter import edge_filter
from filters.filter_types.grayscale_filter import grayscale_filter
from image_handler.image_handler import image_handler

from pages.filter_page import FilterPage
from pages.page_2 import Page2
from pages.profile_page import profile_page

from backend_api.client_api import client_api

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.api = client_api("http://localhost:3000")
        
        # Shared objects
        self.factory = filter_factory()
        self.factory.add_filter("blur", blur_filter())
        self.factory.add_filter("edge", edge_filter())
        self.factory.add_filter("sepia", sepia_filter())
        self.factory.add_filter("grayscale", grayscale_filter())
        self.handler = image_handler()

        # Initialize pages
        self.filter_page = FilterPage(self.factory, self.handler)  # <-- new FilterPage
        self.page2 = Page2(self.ui.gallery_pg)  # assuming page2 still uses Designer widget
        self.profile_page = profile_page(self.ui.profile_pg, self.api)

        # Add filter_page to the main stacked widget
        self.ui.windows.addWidget(self.filter_page)

        # Sidebar button navigation
        self.ui.filter_pg_btn.clicked.connect(
            lambda: self.ui.windows.setCurrentWidget(self.filter_page)
        )
        
        self.ui.profile_pg_btn.clicked.connect(
            lambda: self.ui.windows.setCurrentWidget(self.ui.profile_pg)
        )

        # Set initial page
        self.ui.windows.setCurrentWidget(self.filter_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
