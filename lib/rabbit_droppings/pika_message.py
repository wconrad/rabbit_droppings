from message import Message


class PikaMessage:

    def __init__(self, delivery_info, properties, body):
        self._delivery_info = delivery_info
        self._properties = properties
        self._body = body

    def to_message(self):
        message = Message()
        message.body = self._body
        message.properties = {
            "content_encoding": self._properties.content_encoding,
            "headers": self._properties.headers,
            "delivery_mode": self._properties.delivery_mode,
            "priority": self._properties.priority,
            "correlation_id": self._properties.correlation_id,
            "reply_to": self._properties.reply_to,
            "expiration": self._properties.expiration,
            "message_id": self._properties.message_id,
            "timestamp": self._properties.timestamp,
            "type": self._properties.type,
            "user_id": self._properties.user_id,
            "app_id": self._properties.app_id,
            "cluster_id": self._properties.cluster_id,
            }
        message.delivery_info = {
            "delivery_tag": self._delivery_info.delivery_tag
        }
        return message
