class Message:

    def __init__(self,
                 body='',
                 properties=None):
        self.body = body
        if properties is None:
            properties = {}
        self.properties = properties

    def attrs(self):
        return self.__dict__

    def to_message(self):
        return self
