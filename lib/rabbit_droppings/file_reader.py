from reader import Reader


class FileReader:
    """Read rabbit messages from a file."""

    def __init__(self, path):
        """Create a new instance given the path of the file."""
        input = open(path, "r")
        self._reader = Reader(input)

    def close(self):
        """Close the reader.  Once closed, it must not be used."""
        self._reader.close()

    def read(self):
        """Read a message from the file.  Returns a Message"""
        return self._reader.read()
