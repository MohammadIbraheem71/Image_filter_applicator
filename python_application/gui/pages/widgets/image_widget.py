from ui_py.widgets.image_widget import Ui_image_widget
from .image_widget_base import image_widget_base


#inherits from the base class, loads its own ui
class image_widget(image_widget_base):
    def __init__(self, url, likes=0, image_id=None, api=None, liked_by_user=False):
        super().__init__(url, likes, image_id, api, liked_by_user)
        
        # Load this widget's UI file
        self.ui = Ui_image_widget()
        self.ui.setupUi(self)
        
        #call base class set up ui
        self.setup_widget()