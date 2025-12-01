from utils.event_bus import event_bus


#event listner class, registers a callback for one specific event
class event_listner:
    def __init__(self, event_name: str, callback):
        print(f"registered a listner, listening to {event_name}")
        self.event_name = event_name
        self.callback = callback
        event_bus.subscribe(self._internal_callback)

    def _internal_callback(self, received_event_name, payload):
        if received_event_name == self.event_name:
            self.callback(payload)
