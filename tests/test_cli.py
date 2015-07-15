import test_setup  # noqa

import json
import os
import subprocess
import sys
import unittest

import captive_rabbit.rabbit
import rabbit_droppings


class TestCli(unittest.TestCase):

    def setUp(self):
        self.captive_rabbit = captive_rabbit.Rabbit()
        rabbit_config = rabbit_droppings._RabbitConfig()
        rabbit_config.host = self.captive_rabbit.host
        self.rabbit = rabbit_droppings._Rabbit(rabbit_config)

    def tearDown(self):
        self.captive_rabbit.teardown()

    def test_dump(self):
        captive_queue = self.captive_rabbit.make_queue()
        captive_queue.publish("foo")
        args = [
            self.cli_path(),
            '--host', 'localhost',
            '--queue', captive_queue.name,
            '--file', '/dev/stdout',
            '--dump',
            ]
        process = subprocess.Popen(args,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        output = process.communicate()[0]
        lines = output.splitlines()
        dicts = map(lambda line: json.loads(line), lines)
        bodies = map(lambda json: json['body'], dicts)
        self.assertEquals(bodies, ['foo'])
        self.assertEquals(captive_queue.read().body, "foo")

    def test_purge(self):
        captive_queue = self.captive_rabbit.make_queue()
        captive_queue.publish("foo")
        args = [
            self.cli_path(),
            '--host', 'localhost',
            '--queue', captive_queue.name,
            '--file', '/dev/stdout',
            '--purge',
            ]
        process = subprocess.Popen(args,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        output = process.communicate()[0]
        lines = output.splitlines()
        dicts = map(lambda line: json.loads(line), lines)
        bodies = map(lambda json: json['body'], dicts)
        self.assertEquals(bodies, ['foo'])
        self.assertEquals(captive_queue.read(), None)

    def test_restore(self):
        captive_queue = self.captive_rabbit.make_queue()
        args = [
            self.cli_path(),
            '--host', 'localhost',
            '--queue', captive_queue.name,
            '--file', '/dev/stdin',
            '--restore',
            ]
        process = subprocess.Popen(args,
                                   stdin=subprocess.PIPE)
        record = {
            "body": "foo",
            }
        input = json.dumps(record) + "\n"
        process.communicate(input)
        self.assertEquals(captive_queue.read().body, "foo")
        self.assertEquals(captive_queue.read(), None)

    def cli_path(self):
        return os.path.dirname(os.path.realpath(__file__)) + '/../bin/rabbit_droppings'

if __name__ == '__main__':
    unittest.main()
