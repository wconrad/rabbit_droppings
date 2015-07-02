class Message:

    def __init__(self, method_frame, header_frame, body):
        self._method_frame = method_frame
        self._header_frame = header_frame
        self.body = body
