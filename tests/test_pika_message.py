import test_setup  # noqa

import pika
import rabbit_droppings
import time
import unittest

class TestPikaMessage(unittest.TestCase):

    class StubGetOk:
        def __init__(self, delivery_tag):
            self.delivery_tag = delivery_tag

    def test_defaults(self):
        msg = rabbit_droppings.PikaMessage("foo")
        self.assertEqual(msg.body, "foo")

    def test_to_message(self):
        now = time.time()
        delivery_info = pika.spec.Basic.GetOk(
            delivery_tag='deltag',
            )
        properties = pika.BasicProperties(
            content_type='text/plain',
            content_encoding='8BIT',
            headers={'foo': 'bar'},
            delivery_mode=2,
            priority=0,
            correlation_id='abc123',
            reply_to='reply_queue',
            expiration=12345678,
            message_id='def456',
            timestamp=now,
            type='test_message',
            user_id='guest',
            app_id='foo.py',
            cluster_id='cluster1')
        body = 'Your ad in this spot'
        pika_message = rabbit_droppings.PikaMessage(body,
                                                    properties=properties,
                                                    delivery_info=delivery_info)
        message = pika_message.to_message()
        self.assertEqual(message.body, 'Your ad in this spot')
        self.assertEqual(message.properties['content_type'], 'text/plain')
        self.assertEqual(message.properties['content_encoding'], '8BIT')
        self.assertEqual(message.properties['headers'], {'foo': 'bar'})
        self.assertEqual(message.properties['delivery_mode'], 2)
        self.assertEqual(message.properties['priority'], 0)
        self.assertEqual(message.properties['correlation_id'], 'abc123')
        self.assertEqual(message.properties['reply_to'], 'reply_queue')
        self.assertEqual(message.properties['expiration'], 12345678)
        self.assertEqual(message.properties['message_id'], 'def456')
        self.assertEqual(message.properties['timestamp'], now)
        self.assertEqual(message.properties['type'], 'test_message')
        self.assertEqual(message.properties['user_id'], 'guest')
        self.assertEqual(message.properties['app_id'], 'foo.py')
        self.assertEqual(message.properties['cluster_id'], 'cluster1')
        self.assertEqual(message.delivery_info['delivery_tag'], 'deltag')

if __name__ == '__main__':
    unittest.main()
