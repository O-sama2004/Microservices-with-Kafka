import threading
from .consumer import start_consumer  # Kafka consumer

class ReceiverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'receiver'

    def ready(self):
        thread = threading.Thread(target=start_consumer)
        thread.daemon = True
        thread.start()