import test_setup  # noqa

import math
import pika
import time
import unittest

import captive_rabbit.rabbit
import rabbit_droppings


class TestRabbit(unittest.TestCase):

    def setUp(self):
        self.captive_rabbit = captive_rabbit.Rabbit()
        rabbit_config = rabbit_droppings.RabbitConfig()
        rabbit_config.host = self.captive_rabbit.host
        self.rabbit = rabbit_droppings.Rabbit(rabbit_config)

    def tearDown(self):
        self.captive_rabbit.teardown()

    def test_read_without_ack(self):
        captive_queue = self.captive_rabbit.make_queue()
        captive_queue.publish("foo")
        captive_queue.publish("bar")
        queue = self.rabbit.queue(captive_queue.name)
        self.assertEquals(queue.read().body, "foo")
        self.assertEquals(queue.read().body, "bar")
        self.assertEquals(queue.read(), None)
        self.rabbit.disconnect()
        self.assertEquals(captive_queue.read().body, "foo")

    def test_read_with_ack(self):
        captive_queue = self.captive_rabbit.make_queue()
        captive_queue.publish("foo")
        captive_queue.publish("bar")
        queue = self.rabbit.queue(captive_queue.name)
        self.assertEquals(self.read_and_ack(queue).body, "foo")
        self.assertEquals(self.read_and_ack(queue).body, "bar")
        self.assertEquals(queue.read(), None)
        self.rabbit.disconnect()
        self.assertEquals(captive_queue.read(), None)

    def test_read_properties(self):
        now = math.floor(time.time())
        properties = pika.BasicProperties(
            content_type='text/plain',
            content_encoding='8BIT',
            headers={'foo': 'bar'},
            delivery_mode=2,
            priority=0,
            correlation_id='abc123',
            reply_to='reply_queue',
            expiration='12345678',
            message_id='def456',
            timestamp=now,
            type='test_message',
            user_id='guest',
            app_id='foo.py',
            cluster_id='cluster1')
        captive_queue = self.captive_rabbit.make_queue()
        captive_queue.publish("foo", properties=properties)
        queue = self.rabbit.queue(captive_queue.name)
        message = self.read_and_ack(queue)
        self.assertEqual(message.body, "foo")
        self.assertEqual(message.properties['content_type'], 'text/plain')
        self.assertEqual(message.properties['content_encoding'], '8BIT')
        self.assertEqual(message.properties['headers'], {'foo': 'bar'})
        self.assertEqual(message.properties['delivery_mode'], 2)
        self.assertEqual(message.properties['priority'], 0)
        self.assertEqual(message.properties['correlation_id'], 'abc123')
        self.assertEqual(message.properties['reply_to'], 'reply_queue')
        self.assertEqual(message.properties['expiration'], '12345678')
        self.assertEqual(message.properties['message_id'], 'def456')
        self.assertEqual(message.properties['timestamp'], now)
        self.assertEqual(message.properties['type'], 'test_message')
        self.assertEqual(message.properties['user_id'], 'guest')
        self.assertEqual(message.properties['app_id'], 'foo.py')
        self.assertEqual(message.properties['cluster_id'], 'cluster1')

    def test_write(self):
        captive_queue = self.captive_rabbit.make_queue()
        queue = self.rabbit.queue(captive_queue.name)
        queue.publish(rabbit_droppings.Message("foo"))
        queue.publish(rabbit_droppings.Message("bar"))
        self.rabbit.disconnect()
        self.assertEquals(captive_queue.read().body, "foo")
        self.assertEquals(captive_queue.read().body, "bar")
        self.assertEquals(captive_queue.read(), None)

    def test_write_attributes(self):
        captive_queue = self.captive_rabbit.make_queue()
        queue = self.rabbit.queue(captive_queue.name)
        message = rabbit_droppings.Message()
        message.body = "body"
        now = math.floor(time.time())
        message.properties = {
            'content_type': 'text/plain',
            'content_encoding': '8BIT',
            'headers': {'foo': 'bar'},
            'delivery_mode': 2,
            'priority': 0,
            'correlation_id': 'abc123',
            'reply_to': 'reply_queue',
            'expiration': '12345678',
            'message_id': 'def456',
            'timestamp': now,
            'type': 'test_message',
            'user_id': 'guest',
            'app_id': 'foo.py',
            'cluster_id': 'cluster1',
            }
        queue.publish(message)
        self.rabbit.disconnect()
        message = captive_queue.read()
        self.assertEquals(message.body, "body")
        self.assertEquals(message.properties.content_type, 'text/plain')
        self.assertEquals(message.properties.content_encoding, '8BIT')
        self.assertEquals(message.properties.headers, {'foo': 'bar'})
        self.assertEquals(message.properties.delivery_mode, 2)
        self.assertEquals(message.properties.priority, 0)
        self.assertEquals(message.properties.correlation_id, 'abc123')
        self.assertEquals(message.properties.reply_to, 'reply_queue')
        self.assertEquals(message.properties.expiration, '12345678')
        self.assertEquals(message.properties.message_id, 'def456')
        self.assertEquals(message.properties.timestamp, now)
        self.assertEquals(message.properties.type, 'test_message')
        self.assertEquals(message.properties.user_id, 'guest')
        self.assertEquals(message.properties.app_id, 'foo.py')
        self.assertEquals(message.properties.cluster_id, 'cluster1')

    def read_and_ack(self, queue):
        message = queue.read()
        queue.ack(message)
        return message

    def make_message(self, body):
        message = rabbit_droppings.Message()
        message.body = body
        return message

if __name__ == '__main__':
    unittest.main()
