import test_setup

import StringIO
import rabbit_droppings
import unittest

class TestReaderWriter(unittest.TestCase):

    def test_round_trip(self):
        io = StringIO.StringIO()
        message_out = rabbit_droppings.Message()
        message_out.payload = "payload goes here"
        message_out.properties = {"headers": {"foo": "bar"}}
        writer = rabbit_droppings.Writer(io)
        writer.write(message_out) 
        io.seek(0)
        reader = rabbit_droppings.Reader(io)
        message_in = reader.read()
        self.assertEquals(message_out.payload, message_in.payload)
        self.assertEquals(message_out.properties, message_in.properties)
 
if __name__ == '__main__':
    unittest.main()
