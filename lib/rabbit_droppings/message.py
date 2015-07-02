class Message:

    def __init__(self,
                 body='',
                 delivery_info=None,
                 properties=None):
        self.body = body
        if delivery_info is None:
            delivery_info = {}
        if properties is None:
            properties = {}
        self.delivery_info = {}
        self.properties = properties

    def attrs(self):
        return self.__dict__

    def to_message(self):
        return self
