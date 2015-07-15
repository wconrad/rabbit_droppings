#!/usr/bin/env python

from setuptools import setup
import rabbit_droppings

SCRIPTS = [
    'bin/rabbit_droppings',
]

setup(
    author='Wayne Conrad',
    author_email='kf7qga@gmail.com',
    description='Backup/Restore RabbitMQ queues',
    long_description_markdown_filename='README.markdown',
    name=rabbit_droppings.NAME,
    version=rabbit_droppings.VERSION,
    packages=['lib/rabbit_droppings'],
    setup_requires=['setuptools-markdown'],
    scripts=SCRIPTS,
    install_requires=[
        # Pika does not use semantic versioning.  Breaking changes may
        # be introduced with a bump in patch level, which is why we
        # ask for an exact patch level.
        "pika==0.9.14",
    ],
    test_suite="tests",
)
