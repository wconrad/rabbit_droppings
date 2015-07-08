import test_setup  # noqa

import pika
import rabbit_droppings
import time
import unittest

class TestMessage(unittest.TestCase):

    def test_to_pika_message(self):
        now = time.time()
        delivery_info = {
            'delivery_tag': 'deltag'
            }
        properties = {
            'content_type': 'text/plain',
            'content_encoding': '8BIT',
            'headers': {'foo': 'bar'},
            'delivery_mode': 2,
            'priority': 0,
            'correlation_id': 'abc123',
            'reply_to': 'reply_queue',
            'expiration': 12345678,
            'message_id': 'def456',
            'timestamp': now,
            'type': 'test_message',
            'user_id': 'guest',
            'app_id': 'foo.py',
            'cluster_id': 'cluster1',
            }
        body = 'Your ad in this spot'
        message = rabbit_droppings.Message(body, delivery_info, properties)
        pika_message = message.to_pika_message()
        self.assertEqual(pika_message.body, 'Your ad in this spot')
        self.assertEqual(pika_message.properties.content_type, 'text/plain')
        self.assertEqual(pika_message.properties.content_encoding, '8BIT')
        self.assertEqual(pika_message.properties.headers, {'foo': 'bar'})
        self.assertEqual(pika_message.properties.delivery_mode, 2)
        self.assertEqual(pika_message.properties.priority, 0)
        self.assertEqual(pika_message.properties.correlation_id, 'abc123')
        self.assertEqual(pika_message.properties.reply_to, 'reply_queue')
        self.assertEqual(pika_message.properties.expiration, 12345678)
        self.assertEqual(pika_message.properties.message_id, 'def456')
        self.assertEqual(pika_message.properties.timestamp, now)
        self.assertEqual(pika_message.properties.type, 'test_message')
        self.assertEqual(pika_message.properties.user_id, 'guest')
        self.assertEqual(pika_message.properties.app_id, 'foo.py')
        self.assertEqual(pika_message.properties.cluster_id, 'cluster1')
        self.assertEqual(pika_message.delivery_info.delivery_tag, 'deltag')

    def test_to_pika_message_when_empty(self):
        delivery_info = {}
        properties = {}
        body = 'Your ad in this spot'
        message = rabbit_droppings.Message(body, delivery_info, properties)
        pika_message = message.to_pika_message()
        self.assertEqual(pika_message.body, 'Your ad in this spot')
        self.assertEqual(pika_message.properties.content_type, None)
        self.assertEqual(pika_message.properties.content_encoding, None)
        self.assertEqual(pika_message.properties.headers, None)
        self.assertEqual(pika_message.properties.delivery_mode, None)
        self.assertEqual(pika_message.properties.priority, None)
        self.assertEqual(pika_message.properties.correlation_id, None)
        self.assertEqual(pika_message.properties.reply_to, None)
        self.assertEqual(pika_message.properties.expiration, None)
        self.assertEqual(pika_message.properties.message_id, None)
        self.assertEqual(pika_message.properties.timestamp, None)
        self.assertEqual(pika_message.properties.type, None)
        self.assertEqual(pika_message.properties.user_id, None)
        self.assertEqual(pika_message.properties.app_id, None)
        self.assertEqual(pika_message.properties.cluster_id, None)
        self.assertEqual(pika_message.delivery_info.delivery_tag, None)

if __name__ == '__main__':
    unittest.main()
