from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QRectF, QThreadPool
from PySide6.QtGui import QPixmap, QImage, QPainter, QPainterPath
import requests
from io import BytesIO
from PIL import Image

from utils.image_worker import image_worker
from utils.event_bus import event_bus


class image_widget_base(QWidget):

    def __init__(self, url, likes=0, image_id=None, api=None, liked_by_user=False):
        super().__init__()
        self.ui = None  # Will be set by subclasses
        
        self.thread_pool = QThreadPool.globalInstance()
        self.image_id = image_id
        self.api = api
        self.liked_by_user = liked_by_user
        self.likes = likes
        self.original_pixmap = None
        self.url = url

    #this is called after setupUI, sets up the connections and signals and all
    def setup_widget(self):
        self.ui.img_lbl.setScaledContents(False)
        
        #initialize the button states
        self._update_like_button_state()

        # Connect signals
        self.ui.like_btn.clicked.connect(self.toggle_like)
        self.ui.liked_btn.clicked.connect(self.toggle_like)
        self.ui.like_count.setText(str(self.likes))
        self.ui.magnify_btn.clicked.connect(self.emit_magnify_signal)

        #we load the image
        self.load_image_async(self.url)

        #disable like toke for guests
        if self.api.token == None:
            self.disable_like_button()

    #uses our own event bus to emit the magnify signal;
    def emit_magnify_signal(self):
        event_bus.emit(event_name="request_magnify", payload={"image_id": self.image_id})

    def disable_like_button(self):
        self.ui.like_btn.setEnabled(False)
        self.ui.liked_btn.setEnabled(False)
        self.ui.liked_btn.setVisible(False)


    def _update_like_button_state(self):
        if not self.api or not self.api.token:
            #disable like and liked button for users that havent signed in
            self.ui.like_btn.setEnabled(False)
            self.ui.liked_btn.setEnabled(False)
        else:
            #if signed in then toggle n stuff
            if self.liked_by_user:
                self.ui.like_btn.setVisible(False)
                self.ui.liked_btn.setVisible(True)
            else:
                self.ui.like_btn.setVisible(True)
                self.ui.liked_btn.setVisible(False)

    #this fucntion handles the like and unlike logic
    def toggle_like(self):
        if not self.api or not self.image_id:
            print("API instance or image ID missing")
            return

        try:
            if self.ui.like_btn.isVisible():
                #attempt to like
                res = self.api.like_image(self.image_id)
                if res.get("success"):
                    self.likes += 1
                    self.liked_by_user = True
                    self.ui.like_btn.setVisible(False)
                    self.ui.liked_btn.setVisible(True)
            else:
                #attempt to unlike
                res = self.api.unlike_image(self.image_id)
                if res.get("success"):
                    self.likes -= 1
                    self.liked_by_user = False
                    self.ui.like_btn.setVisible(True)
                    self.ui.liked_btn.setVisible(False)

            self.ui.like_count.setText(str(self.likes))

        except Exception as e:
            print(f"Error toggling like: {e}")

    #async loader function, uses the thread that we created
    def load_image_async(self, url):
        worker = image_worker(url)
        worker.signals.finished.connect(self.on_image_fetched)
        worker.signals.error.connect(self.on_image_error)
        self.thread_pool.start(worker)

    #this is called when the thread finishes working. displays the image
    def on_image_fetched(self, pil_image):
        pixmap = self.pil_to_qpixmap(pil_image)
        self.original_pixmap = pixmap
        self.update_image_display()

    def on_image_error(self, error):
        print(f"Failed to load image (something went wrong with the threading part): {error}")
        self.ui.img_lbl.setText("Image failed to load")

    #this isnt used anymore, use the async function for non blocking behaviour
    def load_image(self, url: str):
        try:
            response = requests.get(url)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content)).convert("RGBA")
            pixmap = self.pil_to_qpixmap(image)
            
            self.original_pixmap = pixmap
            self.update_image_display()
            
        except Exception as e:
            print(f"Failed to load image from {url}: {e}")
            self.ui.img_lbl.setText("Image failed to load")

    #do not tinker with these functions, these only display the images
    #took a lot of time to get right, please pangay mat lena
    def update_image_display(self):
        lbl = self.ui.img_lbl
        # Must have a valid original image and non-zero dimensions
        if self.original_pixmap and lbl.width() > 0 and lbl.height() > 0:
            print(f"label width = {lbl.width()}, label height = {lbl.height()}")
            target_w = lbl.width()
            target_h = lbl.height()
            radius = 12

            # Scale for "Cover" effect
            scaled_pixmap = self.original_pixmap.scaled(
                target_w,
                target_h,
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            # Calculate the offset to center the scaled pixmap (cropping effect)
            x_offset = int((target_w - scaled_pixmap.width()) / 2)
            y_offset = int((target_h - scaled_pixmap.height()) / 2)
            
            # Clip, round, and display
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
    def _clip_and_round_pixmap(self, source_pixmap: QPixmap, target_w: int, target_h: int, 
                               draw_x: int, draw_y: int, radius: int) -> QPixmap:
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
        path.arcTo(rect.left(), rect.top(), radius * 2, radius * 2, 180, -90)  # Top-left
        path.lineTo(rect.right() - radius, rect.top())
        path.arcTo(rect.right() - radius * 2, rect.top(), radius * 2, radius * 2, 90, -90)  # Top-right
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