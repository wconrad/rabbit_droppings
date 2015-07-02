from pika_message import PikaMessage


class Queue:

    def __init__(self, channel, name):
        self._channel = channel
        self.name = name

    def publish(self, body):
        self._channel.basic_publish(exchange='',
                                    routing_key=self.name,
                                    body=body)

    def read(self):
        method_frame, header_frame, body = self._channel.basic_get(self.name)
        if method_frame:
            message = PikaMessage(header_frame, body).to_message()
            self._channel.basic_ack(method_frame.delivery_tag)
            return message
        else:
            return None
