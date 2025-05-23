class EventManager:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify(self, event: str, data: dict):
        for obs in self._observers:
            obs.update(event, data)

# Instancia global de eventos
event_manager = EventManager()
