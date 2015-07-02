import test_setup   # noqa

import rabbit_droppings
import tempfile
import unittest


class TestFileWriter(unittest.TestCase):

    def test_round_trip(self):
        path = self.make_temp_path()
        file_writer = rabbit_droppings.FileWriter(path)
        file_writer.write(self.make_message("1"))
        file_writer.write(self.make_message("2"))
        file_reader = rabbit_droppings.FileReader(path)
        self.assertEquals(file_reader.read().body, "1")
        self.assertEquals(file_reader.read().body, "2")
        self.assertEquals(file_reader.read(), None)

    def test_close(self):
        path = self.make_temp_path()
        file_writer = rabbit_droppings.FileWriter(path)
        file_writer.write(self.make_message("1"))
        file_writer.write(self.make_message("2"))
        file_reader = rabbit_droppings.FileReader(path)
        self.assertEquals(file_reader.read().body, "1")
        file_reader.close()
        self.assertRaises(ValueError, file_reader.read)

    def make_temp_path(self):
        tf = tempfile.NamedTemporaryFile()
        path = tf.name
        tf.close()
        return path

    def make_message(self, body):
        message = rabbit_droppings.Message()
        message.body = body
        return message

if __name__ == '__main__':
    unittest.main()
