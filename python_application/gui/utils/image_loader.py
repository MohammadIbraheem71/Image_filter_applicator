# utils/image_loader.py
from PySide6.QtWidgets import QWidget, QGridLayout
from pages.widgets.image_widget import image_widget
from PySide6.QtCore import Qt, QRectF, QThreadPool, Signal
from utils.flowlayout import flowlayout
#this class is responsible for loading image_widgets into the layout grid for the gallery or 
#any other scroll area
#an api object is passed in to manage the loading from db
#standard image loader
class image_loader:

    def __init__(self, container_widget: QWidget, columns: int = 3, api=None, widget_cls = None):
        self.container = container_widget
        self.layout = self.container.layout()
        self.container.setLayout(self.layout)
        self.columns = columns
        self.api = api 

        self.widget_cls = widget_cls or self.default_widget_class()


        #this replaces the existing grid layout with the flow layout tthat manages this dynamic layout stuff

        if self.layout is None or not isinstance(self.layout, flowlayout):
            self.layout = flowlayout()
            self.container.setLayout(self.layout)

    #if no widget is provided, then load the widget without trash
    def default_widget_class(self):
        print("using the default image_widget")
        from pages.widgets.image_widget import image_widget
        return image_widget
    
    #utility function to clear all previous images
    def clear_layout(self):
        
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    #this function is responsible for the loading of the images
    #the images are now passed in as a parameter
    # def load_images(self, images): 
    #     if images is None:
    #         print("No images provided to load.")
    #         return

    #     self.clear_layout()

    #     row, col = 0, 0
    #     for item in images:
    #         image_url = item.get("image_url")
    #         image_id = item.get("id")
    #         likes = item.get("likes", 0)
    #         liked_by_user = item.get("liked_by_user", False)

    #         # Create widget
    #         img_card = self.widget_cls(
    #             url=image_url,
    #             likes=likes,
    #             image_id=image_id,
    #             api=self.api,
    #             liked_by_user=liked_by_user
    #         )

    #         # Disable like button if user not signed in
    #         if not getattr(self.api, "token", None):
    #             img_card.disable_like_button()

    #         # Add to layout
    #         self.layout.addWidget(img_card, row, col)

    #         col += 1
    #         if col >= self.columns:
    #             col = 0
    #             row += 1

    def load_images(self, images):
        if images is None:
            return

        self.clear_layout()

        for item in images:
            image_url = item.get("image_url")
            image_id = item.get("id")
            likes = item.get("likes", 0)
            liked_by_user = item.get("liked_by_user", False)

            img_card = self.widget_cls(
                url=image_url,
                likes=likes,
                image_id=image_id,
                api=self.api,
                liked_by_user=liked_by_user
            )

            if not getattr(self.api, "token", None):
                img_card.disable_like_button()

            self.layout.addWidget(img_card)
