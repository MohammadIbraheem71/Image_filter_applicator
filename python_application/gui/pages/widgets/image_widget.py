from PySide6.QtWidgets import QWidget, QLabel, QSizePolicy, QVBoxLayout 
from PySide6.QtCore import Qt, QRectF, QThreadPool
from PySide6.QtGui import QPixmap, QImage, QPainter, QPainterPath
import requests
from io import BytesIO
from PIL import Image

from ui_py.widgets.image_widget import Ui_image_widget
from utils.image_worker import image_worker

#this widget houses the image, and related buttons.
class image_widget(QWidget):
    def __init__(self, url, likes=0, image_id=None, api=None, liked_by_user=False):
        super().__init__()
        self.ui = Ui_image_widget()
        self.ui.setupUi(self)
        
        self.thread_pool = QThreadPool.globalInstance()

        self.image_id = image_id
        self.api = api
        self.liked_by_user = liked_by_user
        self.likes = likes
        self.original_pixmap = None  
        
        # # 2. Ensure the parent layout allocates more height to the image
        # parent_layout = self.layout()
        # if parent_layout and isinstance(parent_layout, QVBoxLayout):
        #     # Assuming the image label is index 0 and the info widget is index 1
        #     parent_layout.setStretch(0, 3) 
        #     parent_layout.setStretch(1, 1)
        # # ------------------------------

        # --- IMPORTANT: Ensure setScaledContents is OFF! ---
        # We handle scaling manually in update_image_display
        self.ui.img_lbl.setScaledContents(False) 
        
        #here we initialize the like button state
        self._update_like_button_state()

        self.ui.like_btn.clicked.connect(self.toggle_like)
        self.ui.liked_btn.clicked.connect(self.toggle_like)
        self.ui.like_count.setText(str(self.likes))


        self.load_image_async(url)

    #this function disables the like button for guest users
    def disable_like_button(self):
        self.ui.like_btn.setEnabled(False)
        self.ui.liked_btn.setEnabled(False)
        self.ui.liked_btn.setVisible(False)
    #this button sets the initial like button state based on the input
    #wether the user has already liked the image or not
    def _update_like_button_state(self):
            if not self.api or not self.api.token:
                # User not signed in → disable like button
                self.ui.like_btn.setEnabled(False)
                self.ui.liked_btn.setEnabled(False)
            else:
                # Signed in → toggle buttons based on liked_by_user
                if self.liked_by_user:
                    self.ui.like_btn.setVisible(False)
                    self.ui.liked_btn.setVisible(True)
                else:
                    self.ui.like_btn.setVisible(True)
                    self.ui.liked_btn.setVisible(False)

    #this handles the like and unlike logic 
    def toggle_like(self):
        if not self.api or not self.image_id:
            print("API instance or image ID missing")
            return

        try:
            if self.ui.like_btn.isVisible():
                # Attempt to like
                res = self.api.like_image(self.image_id)
                if res.get("success"):
                    self.likes += 1
                    self.liked_by_user = True
                    self.ui.like_btn.setVisible(False)
                    self.ui.liked_btn.setVisible(True)
            else:
                # Attempt to unlike
                res = self.api.unlike_image(self.image_id)
                if res.get("success"):
                    self.likes -= 1
                    self.liked_by_user = False
                    self.ui.like_btn.setVisible(True)
                    self.ui.liked_btn.setVisible(False)

            self.ui.like_count.setText(str(self.likes))

        except Exception as e:
            print(f"Error toggling like: {e}")

    #this is the async image loading function
    #hopefully it does not block the main thread
    def load_image_async(self, url):
        worker = image_worker(url)
        worker.signals.finished.connect(self.on_image_fetched)
        worker.signals.error.connect(self.on_image_error)
        self.thread_pool.start(worker)

    #once the thread is done working, it calls this function, this displays the image
    def on_image_fetched(self, pil_image):
        pixmap = self.pil_to_qpixmap(pil_image)
        self.original_pixmap = pixmap
        self.update_image_display()

    #called by the thread in case of error
    def on_image_error(self, error):
        print(f"Failed to load image (something went wrong with the threading part): {error}")
        self.ui.img_lbl.setText("Image failed to load")

    #this function loads the image
    def load_image(self, url: str):
        try:
            response = requests.get(url)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content)).convert("RGBA")
            pixmap = self.pil_to_qpixmap(image)
            
            self.original_pixmap = pixmap
            # Call update_image_display() to scale and display the image
            # This is sufficient if the widget size is guaranteed not to change
            self.update_image_display() 
            
        except Exception as e:
            print(f"Failed to load image from {url}: {e}")
            self.ui.img_lbl.setText("Image failed to load")
    
    
    #do not tinker with these functions, these only display the images
    #took a lot of time to get right, please pangay mat lena
    def update_image_display(self):
        """
        Performs the 3 steps: 
        1. Gets label size. 
        2. Scales the original pixmap to "cover" the label area (cropping).
        3. Applies custom rounding and displays the result.
        """
        lbl = self.ui.img_lbl
        # Must have a valid original image and non-zero dimensions
        if self.original_pixmap and lbl.width() > 0 and lbl.height() > 0:
            # 1. Get label size
            print(f"label width = {lbl.width()}, label height = {lbl.height()}")
            target_w = lbl.width()
            target_h = lbl.height()
            radius = 12 

            # 2. Scale for "Cover" effect (Qt.KeepAspectRatioByExpanding)
            scaled_pixmap = self.original_pixmap.scaled(
                target_w,
                target_h,
                Qt.KeepAspectRatioByExpanding, 
                Qt.SmoothTransformation
            )

            # Calculate the offset to center the scaled pixmap (cropping effect)
            x_offset = int((target_w - scaled_pixmap.width()) / 2)
            y_offset = int((target_h - scaled_pixmap.height()) / 2)
            
            # 3. Clip, round, and display
            rounded_pixmap = self._clip_and_round_pixmap(
                source_pixmap=scaled_pixmap, 
                target_w=target_w, 
                target_h=target_h, 
                draw_x=x_offset, 
                draw_y=y_offset, 
                radius=radius
            )
            
            lbl.setPixmap(rounded_pixmap)
            lbl.setAlignment(Qt.AlignCenter) 
            
    
    #dont bother with this function either, took a lot of time to get right
    #please pangay mat lena
    def _clip_and_round_pixmap(self, source_pixmap: QPixmap, target_w: int, target_h: int, draw_x: int, draw_y: int, radius: int) -> QPixmap:
        """
        Creates a final pixmap (target_w x target_h) with rounded top corners, 
        drawing the source_pixmap at the specified offset (for centering/cropping).
        """
        
        final_pixmap = QPixmap(target_w, target_h)
        final_pixmap.fill(Qt.transparent)
        
        painter = QPainter(final_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        rect = QRectF(0, 0, target_w, target_h)
        
        # Create the clipping path (rounded top corners only)
        path = QPainterPath()
        path.moveTo(rect.left(), rect.top() + radius)
        path.arcTo(rect.left(), rect.top(), radius * 2, radius * 2, 180, -90) # Top-left
        path.lineTo(rect.right() - radius, rect.top())
        path.arcTo(rect.right() - radius * 2, rect.top(), radius * 2, radius * 2, 90, -90) # Top-right
        path.lineTo(rect.right(), rect.bottom())
        path.lineTo(rect.left(), rect.bottom())
        path.closeSubpath()
        
        # Clip to the path and draw the centered source pixmap
        painter.setClipPath(path)
        painter.drawPixmap(draw_x, draw_y, source_pixmap)
        
        painter.end()
        
        return final_pixmap
    
    
    @staticmethod
    def pil_to_qpixmap(image: Image.Image) -> QPixmap:
        """Convert a PIL Image to QPixmap."""
        data = image.tobytes("raw", "RGBA")
        qimage = QImage(data, image.width, image.height, QImage.Format_RGBA8888)
        return QPixmap.fromImage(qimage)