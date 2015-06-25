import json

from message import *

class PikaMessage:

    def __init__(self, properties, payload):
        self._properties = properties
        self._payload = payload

    def to_message(self):
        message = Message()
        message.payload = self._payload
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
        return message
