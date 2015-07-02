import test_setup  # noqa

import captive_rabbit.rabbit
import rabbit_droppings
import unittest


class TestRabbit(unittest.TestCase):

    def setUp(self):
        self.captive_rabbit = captive_rabbit.Rabbit()

    def tearDown(self):
        self.captive_rabbit.teardown()

    def test_read(self):
        captive_queue = self.captive_rabbit.make_queue()
        captive_queue.publish("foo")
        captive_queue.publish("bar")
        rabbit_config = rabbit_droppings.RabbitConfig()
        rabbit_config.host = self.captive_rabbit.host
        rabbit = rabbit_droppings.Rabbit(rabbit_config)
        queue = rabbit.queue(captive_queue.name)
        self.assertEquals(queue.read().body, "foo")
        self.assertEquals(queue.read().body, "bar")
        self.assertEquals(queue.read(), None)

if __name__ == '__main__':
    unittest.main()
