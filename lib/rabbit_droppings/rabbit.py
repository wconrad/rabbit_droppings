import pika

from rabbit_droppings.queue import Queue

class Rabbit:

    def __init__(self, config):
        self._config = config
        self._connected = False

    def is_connected(self):
        return self._connected

    def connect(self):
        if self.is_connected():
            return
        params = pika.ConnectionParameters(self._config.host)
        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()
        self._connected = True

    def disconnect(self):
        if not self.is_connected():
            return
        self._connection.close()
        self._connected = False

    def queue(self, name):
        self.connect()
        return Queue(self._channel, name)
