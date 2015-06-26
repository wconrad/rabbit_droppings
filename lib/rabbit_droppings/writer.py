import json

class Writer:

    def __init__(self, output):
        self._output = output

    def write(self, message):
        message = message.to_message()
        attrs = message.attrs()
        json_attrs = json.dumps(attrs)
        self._output.write(json_attrs)
