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
            message = PikaMessage(method_frame,
                                  header_frame,
                                  body).to_message()
            return message
        else:
            return None

    def ack(self, message):
        delivery_tag = message.delivery_info["delivery_tag"]
        self._channel.basic_ack(delivery_tag)

    def publish(self, message):
        pika_message = message.to_pika_message()
        self._channel.basic_publish(exchange='',
                                    routing_key=self.name,
                                    properties=pika_message.properties,
                                    body=message.body)
