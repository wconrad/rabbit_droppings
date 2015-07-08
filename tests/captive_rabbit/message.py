class Message:

    def __init__(self, delivery_info, properties, body):
        self.delivery_info = delivery_info
        self.properties = properties
        self.body = body
