# utils/image_worker.py
from PySide6.QtCore import QObject, QRunnable, Signal, Slot
from PIL import Image
import requests
from io import BytesIO

#made this class for multithreading

class ImageWorkerSignals(QObject):
    finished = Signal(object)  # Emits PIL.Image object
    error = Signal(str)        # Emits error message


#this is supposed to download the image from the url, and then emmits it as a signal.
#intention is to make the main thread non blocking

class image_worker(QRunnable):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.signals = ImageWorkerSignals()

    @Slot()
    def run(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content)).convert("RGBA")
            self.signals.finished.emit(image)
        except Exception as e:
            self.signals.error.emit(str(e))
