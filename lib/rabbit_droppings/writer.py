from __future__ import print_function
import json


class Writer:
    """Writes message to some kind of output.  The messages are written
    in a format that the Reader class can read."""

    def __init__(self, output):
        """Create an instance given an output"""
        self._output = output

    def write(self, message):
        """Write a message to the output."""
        message = message.to_message()
        attrs = message.attrs()
        json_attrs = json.dumps(attrs)
        print(json_attrs, file=self._output)

    def flush(self):
        """Flush the output, ensuring that all messages have been written"""
        self._output.flush()

    def close(self):
        """Close the output.  Do not use after closing."""
        self._output.close()
