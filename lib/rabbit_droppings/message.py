class Message:

    def __init__(self,
                 payload='',
                 properties=None):
        self.payload = payload
        if properties == None:
            properties = {}
        self.properties = properties

    def attrs(self):
        return self.__dict__
