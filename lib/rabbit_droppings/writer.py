from __future__ import print_function
import json

class Writer:

    def __init__(self, output):
        self._output = output

    def write(self, message):
        message = message.to_message()
        attrs = message.attrs()
        json_attrs = json.dumps(attrs)
        print(json_attrs, file=self._output)
