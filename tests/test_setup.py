import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../lib')

import tempfile

def make_temp_path():
    tf = tempfile.NamedTemporaryFile()
    path = tf.name
    tf.close()
    return path
