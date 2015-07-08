class Message:
    """A wrapper around the tuple that pika returns when reading a message.
    """

    def __init__(self, delivery_info, properties, body):
        """
        Args:
          delivery_info [pika.spec.GetOK]
          properties [pika.spec.BasicProperties]
          body [str]
        """
        self.delivery_info = delivery_info
        self.properties = properties
        self.body = body
