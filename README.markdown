This is a Python library and utilities for saving and loading RabbitMQ
messages to and from disk.

**This is a work in progress--it's not ready to use yet.  Check back
later.**

# Why?

* A program cannot publish a message to RabbitMQ, but does not want to
lose the message.  Using this library, the program can save the
message to a file.  Later after fixing the problem, a person can use a
utility in this package to publish the message.

* The consumer has a bug and messages are piling up in a queue.  You
have fixed the bug and your tests seem to indicate the consumer will
now work, but you want some insurance.  Using a program in this
package, you can back up the queue to a file.  If the program
processes the messages incorrectly, you can use use a program in this
package to restore the queue from the file.

# How to save a message from code

## Saving a message with the pika library

If you have a program using the pika library to publish messages to a
RabbitMQ server, here's how to save messages that could not be
published:

First, import the library:

    import rabbit_droppings

If you have a program that needs to save messages that cannot be
published using the pika library, it should create a
rabbit_droppings.Writer (probably in the constructor):

    file = open('/path/to/my/file', 'a')
    self._rd_writer = rabbit_droppings.Writer(file)

When you publish a message and a pika exception occurs, save the
message:

    body = "Message body"
    properties = pika.spec.BasicProperties(
        content_type='text/plain'
        )
    try:
        channel.basic_publish(exchange='',
                              routing_key='some_queue_name',
                              properties=properties,
                              body=body)
    except (pika.exceptions.AMQPError, pika.exceptions.ChannelError) as e:
        pika_message = rabbit_droppings.PikaMessage(body, properties=properties)
        self._rd_writer.write(pika_message)
