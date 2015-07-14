import json

from message import Message


class Reader:
    """Read messages from some kind of input.  The messages should be
    in the format written by the Writer class."""

    def __init__(self, input):
        """Create an instance given a input.  The input should quack
        like a file, responding to readline() and close()."""
        self._input = input

    def close(self):
        """Close the reader.  Do not use after closing."""
        self._input.close()

    def read(self):
        """Read a Message"""
        line = self._input.readline()
        if not line:
            return None
        attrs = json.loads(line)
        return Message(**attrs)
