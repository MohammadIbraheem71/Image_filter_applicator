from ui_py.widgets.image_widget_trash import Ui_image_widget_trash
from .image_widget_base import image_widget_base


class image_widget_trash(image_widget_base):
    """Image widget with trash button that uses shared functionality from base class"""

    def __init__(self, url, likes=0, image_id=None, api=None, liked_by_user=False):
        super().__init__(url, likes, image_id, api, liked_by_user)
        
        # Load this widget's UI file (with trash button)
        self.ui = Ui_image_widget_trash()
        self.ui.setupUi(self)
        
        # Call base class setup to initialize all common functionality
        self.setup_widget()
        
        # Setup trash-specific functionality
        self.setup_trash_button()
    
    def setup_trash_button(self):
        """Connect the trash button signal"""
        self.ui.trash_btn.clicked.connect(self.handle_trash)
    
    def handle_trash(self):
        """Handle trash button click"""
        print(f"Trash clicked for image {self.image_id}")
        
        # Delete the image here
        # e.g., self.api.delete_image(self.image_id)
        # or emit an event: event_bus.emit(event_name="delete_image", payload={"image_id": self.image_id})