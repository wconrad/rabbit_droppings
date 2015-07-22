#!/usr/bin/env python

from setuptools import setup

NAME = "rabbit_droppings"
VERSION = "0.3.0"
SCRIPTS = [
    'bin/rabbit_droppings',
]

setup(
    author='Wayne Conrad',
    author_email='kf7qga@gmail.com',
    description='Backup/Restore RabbitMQ queues',
    install_requires=[
        # Pika does not use semantic versioning.  Breaking changes may
        # be introduced with a bump in patch level, which is why we
        # ask for an exact patch level.
        "pika==0.9.14",
    ],
    keywords = "rabbit rabbitmq backup restore",
    name=NAME,
    packages=['rabbit_droppings'],
    scripts=SCRIPTS,
    test_suite="tests",
    url="https://github.com/wconrad/rabbit_droppings",
    version=VERSION,
)
