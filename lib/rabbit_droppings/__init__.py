"""Package for saving and loading RabbitMQ messages.
"""

from file_reader import FileReader
from file_writer import FileWriter
from message import Message
from pika_message import PikaMessage
from queue import Queue
from rabbit import Rabbit
from rabbit_config import RabbitConfig
from reader import Reader
from writer import Writer

NAME = "rabbit_droppings"
VERSION = "1.0.0"
