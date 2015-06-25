import json

from message import *

class Reader:

    def __init__(self, input):
        self._input = input

    def read(self):
        line = self._input.readline()
        attrs = json.loads(line)
        return Message(**attrs)
