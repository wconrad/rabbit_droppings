from writer import Writer


class FileWriter:
    """Write rabbit messages to a file in a format that the FileReader can
    read"""

    def __init__(self, path):
        """Create a new instance given the path of the file"""
        output = open(path, "w")
        self._writer = Writer(output)

    def write(self, message):
        """Write a Message to the file"""
        self._writer.write(message)

    def flush(self):
        """Flush, ensuring that all messages are written to the file"""
        self._writer.flush()

    def close(self):
        """Close the file.  Do not use after closing"""
        self._writer.close()
