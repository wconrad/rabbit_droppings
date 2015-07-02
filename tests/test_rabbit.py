import test_setup  # noqa

import captive_rabbit.rabbit
import rabbit_droppings
import unittest


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

    def test_write(self):
        captive_queue = self.captive_rabbit.make_queue()
        queue = self.rabbit.queue(captive_queue.name)
        queue.publish(self.make_message("foo"))
        queue.publish(self.make_message("bar"))
        self.rabbit.disconnect()
        self.assertEquals(captive_queue.read().body, "foo")
        self.assertEquals(captive_queue.read().body, "bar")

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
