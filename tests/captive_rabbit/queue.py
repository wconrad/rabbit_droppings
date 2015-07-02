import uuid

from message import Message

class Queue:

    def __init__(self, channel):
        self._channel = channel
        self.name = self._make_unique_name()

    def create(self):
        self._channel.queue_declare(queue=self.name,
                                    durable=False,
                                    auto_delete=True)

    def delete(self):
        self._channel.queue_delete(self.name)

    def publish(self, body):
        self._channel.basic_publish(exchange='',
                                    routing_key=self.name,
                                    body=body)

    def read(self):
        method_frame, header_frame, body = self._channel.basic_get(self.name)
        if method_frame:
            message = Message(method_frame, header_frame, body)
            self._channel.basic_ack(method_frame.delivery_tag)
            return message
        else:
            return None

    def _make_unique_name(self):
        return uuid.uuid4().hex
