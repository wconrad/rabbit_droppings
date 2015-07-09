import uuid

from message import Message


class Queue:

    def __init__(self, rabbit):
        """Create an instance of a queue.  This doesn't create the queue
        on the rabbit server: For that, call .create()."""
        self._rabbit = rabbit
        self.name = self._make_unique_name()

    def create(self):
        """Create the queue"""
        self._channel().queue_declare(queue=self.name,
                                      durable=False,
                                      auto_delete=True)

    def delete(self):
        """Delete the queue"""
        self._channel().queue_delete(self.name)

    def clear(self):
        """Empty the queue by reading and acknowledging all messages"""
        while self.read() is not None:
            pass

    def publish(self, body, properties=None):
        """
        Publish a message
        args:
          body [str]
          properties [pika.spec.BasicProperties]
        """
        self._channel().basic_publish(exchange='',
                                      routing_key=self.name,
                                      properties=properties,
                                      body=body)

    def read(self):
        """Read, and acknowledge, a message.  Returns a
        captive_rabbit.Message,or None if the queue is empty."""
        method_frame, header_frame, body = self._channel().basic_get(self.name)
        if method_frame:
            message = Message(method_frame, header_frame, body)
            self._channel().basic_ack(method_frame.delivery_tag)
            return message
        else:
            return None

    def _make_unique_name(self):
        return uuid.uuid4().hex

    def _channel(self):
        return self._rabbit.channel()
