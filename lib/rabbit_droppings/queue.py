from pika_message import PikaMessage

from rabbit_droppings import FileWriter
from rabbit_droppings import FileReader


class Queue:

    def __init__(self, channel, name):
        self._channel = channel
        self.name = name

    def publish(self, body):
        self._channel.basic_publish(exchange='',
                                    routing_key=self.name,
                                    body=body)

    def read(self):
        """Read and return a Message, or None if the queue is empty.

        The message will not be removed from the queue until it is given to
        the ack method.
        
        Returns: [Message, None]
        """
        method_frame, header_frame, body = self._channel.basic_get(self.name)
        if method_frame:
            pika_message = PikaMessage(body,
                                       delivery_info=method_frame,
                                       properties=header_frame,
                                       )
            return pika_message.to_message()
        else:
            return None

    def ack(self, message, multiple=False):
        """Acknowledge a message.

        Args:
          message [Message]
          multiple [bool] If true, all outstanding messages up to and
            including this message are acknowledged.
        """
        delivery_tag = message.delivery_info["delivery_tag"]
        self._channel.basic_ack(delivery_tag, multiple=multiple)

    def nack(self, message, multiple=False):
        """Negative-acknowledge a message.

        Args:
          message [Message]
          multiple [bool] If true, all outstanding messages up to and
            including this message are acknowledged.
        """
        delivery_tag = message.delivery_info["delivery_tag"]
        self._channel.basic_nack(delivery_tag, multiple=multiple)

    def publish(self, message):
        """Publish a message to the queue.
        
        Args:
          message [Message]
        """
        pika_message = message.to_pika_message()
        self._channel.basic_publish(exchange='',
                                    routing_key=self.name,
                                    properties=pika_message.properties,
                                    body=message.body)

    def dump_to_disk(self, path, destructive=False):
        """Dump the queue to disk.

        Args:
          path [str] The path of the file
          destructive [bool] if true, the queue will be emptied after it is
            successfully dumped.
        """
        file_writer = FileWriter(path)
        try:
            self.dump(file_writer, destructive)
        finally:
            file_writer.close()

    def dump(self, writer, destructive=False):
        """Dump the queue to a Writer."""
        last_msg_written = None
        while True:
            msg = self.read()
            if msg is None:
                break
            writer.write(msg)
            last_msg_written = msg
        if last_msg_written is not None:
            if destructive:
                self.ack(last_msg_written, multiple=True)
            else:
                self.nack(last_msg_written, multiple=True)

    def restore_from_disk(self, path):
        """Restore a queue from a disk file.  This publishes to the queue any
        messages in the disk file.  Any existing messages in the queue will
        still be in the queue.

        Args:
          path [str] The path of the file
        """
        file_reader = FileReader(path)
        try:
            self.restore(file_reader)
        finally:
            file_reader.close()

    def restore(self, reader):
        """Restore a queue from a message reader.  This publishes to the queue
        any messages returned by the reader.  Any existing messages in the queue will
        still be in the queue.

        Args:
          path [str] The path of the file
        """
        while True:
            msg = reader.read()
            if msg is None:
                break
            self.publish(msg)
