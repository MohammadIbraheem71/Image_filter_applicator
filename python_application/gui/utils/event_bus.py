from PySide6.QtCore import QObject, Signal

#singleton 
class event_bus(QObject):
    broadcast = Signal(str, object)

    _instance = None
    _initialized = False  # track if QObject was initialized

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(event_bus, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize QObject only once
        if not self._initialized:
            super().__init__()
            self._initialized = True

    @staticmethod
    def emit(event_name: str, payload=None):
        print(f"emitting a signal, name = {event_name}")
        bus = event_bus()
        bus.broadcast.emit(event_name, payload)

    @staticmethod
    def subscribe(callback):
        bus = event_bus()
        bus.broadcast.connect(callback)
