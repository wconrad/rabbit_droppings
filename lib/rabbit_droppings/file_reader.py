from reader import *

class FileReader:

    def __init__(self, path):
        input = open(path, "r")
        self._reader = Reader(input)

    def close(self):
        self._reader.close()

    def read(self):
        return self._reader.read()
