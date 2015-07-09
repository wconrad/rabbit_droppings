import test_setup  # noqa

import math
import pika
import time
import unittest

import captive_rabbit.rabbit
import rabbit_droppings


class TestQueueBackup(unittest.TestCase):

    def setUp(self):
        self.captive_rabbit = captive_rabbit.Rabbit()
        rabbit_config = rabbit_droppings.RabbitConfig()
        rabbit_config.host = self.captive_rabbit.host
        self.rabbit = rabbit_droppings.Rabbit(rabbit_config)

    def tearDown(self):
        self.captive_rabbit.teardown()

    def test_dump_and_restore_to_disk(self):
        path = test_setup.make_temp_path()
        captive_queue = self.captive_rabbit.make_queue()
        queue = self.rabbit.queue(captive_queue.name)
        captive_queue.publish("foo")
        captive_queue.publish("bar")
        file_writer = rabbit_droppings.FileWriter(path)
        queue.dump_to_disk(path)
        captive_queue.clear()
        self.assertEqual(captive_queue.read(), None)
        queue.restore_from_disk(path)
        self.assertEqual(captive_queue.read().body, "foo")
        self.assertEqual(captive_queue.read().body, "bar")
        self.assertEqual(captive_queue.read(), None)

if __name__ == '__main__':
    unittest.main()
