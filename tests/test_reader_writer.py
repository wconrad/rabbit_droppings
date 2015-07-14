import test_setup  # noqa

import StringIO
import rabbit_droppings
import unittest


class TestReaderWriter(unittest.TestCase):

    def test_round_trip(self):
        path = test_setup.make_temp_path()
        output = open(path, "w")
        file_writer = rabbit_droppings.Writer(output)
        file_writer.write(self.make_message("1"))
        file_writer.write(self.make_message("2"))
        file_writer.close()
        input = open(path, "r")
        file_reader = rabbit_droppings.Reader(input)
        self.assertEquals(file_reader.read().body, "1")
        self.assertEquals(file_reader.read().body, "2")
        self.assertEquals(file_reader.read(), None)
        file_reader.close()

    def test_flush(self):
        path = test_setup.make_temp_path()
        writer = test_setup.make_writer(path)
        reader = test_setup.make_reader(path)
        writer.write(self.make_message("1"), flush=False)
        self.assertEquals(reader.read(), None)
        writer.flush()
        self.assertEquals(reader.read().body, "1")
        writer.close()
        reader.close()

    def test_close_reader(self):
        path = test_setup.make_temp_path()
        writer = test_setup.make_writer(path)
        writer.write(self.make_message("1"))
        writer.write(self.make_message("2"))
        writer.close()
        reader = test_setup.make_reader(path)
        self.assertEquals(reader.read().body, "1")
        reader.close()
        self.assertRaises(ValueError, reader.read)

    def test_close_writer(self):
        path = test_setup.make_temp_path()
        writer = test_setup.make_writer(path)
        reader = test_setup.make_reader(path)
        writer.write(self.make_message("1"), flush=False)
        self.assertEquals(reader.read(), None)
        writer.close()
        self.assertEquals(reader.read().body, "1")
        reader.close()

    def make_message(self, body):
        message = rabbit_droppings.Message()
        message.body = body
        return message

if __name__ == '__main__':
    unittest.main()
