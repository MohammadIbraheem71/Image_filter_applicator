from ui_py.widgets.image_widget_trash import Ui_image_widget_trash
from .image_widget_base import image_widget_base
from utils.event_bus import event_bus

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
        self.ui.trash_btn.clicked.connect(self.emit_delete_signal)
    
    #this emits a delete signal whenver the delete button is clicked, listened to by the profile page to delete the image
    def emit_delete_signal(self):
        event_bus.emit(event_name="request_delete", payload={"image_id": self.image_id})