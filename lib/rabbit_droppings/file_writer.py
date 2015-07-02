from writer import Writer

class FileWriter:

    def __init__(self, path):
        self._path = path

    def write(self, message):
        out = open(self._path, "a")
        try:
            Writer(out).write(message)
        finally:
            out.close()
