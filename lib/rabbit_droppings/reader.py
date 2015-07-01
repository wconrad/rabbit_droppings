import json

from message import *

class Reader:

    def __init__(self, input):
        self._input = input

    def close(self):
        self._input.close()

    def read(self):
        line = self._input.readline()
        if not line:
            return None
        attrs = json.loads(line)
        return Message(**attrs)
