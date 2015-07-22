import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

import rabbit_droppings
import tempfile

def make_temp_path():
    tf = tempfile.NamedTemporaryFile()
    path = tf.name
    tf.close()
    return path

def make_reader(path):
    input = open(path, "r")
    return rabbit_droppings.Reader(input)

def make_writer(path):
    output = open(path, "w")
    return rabbit_droppings.Writer(output)
