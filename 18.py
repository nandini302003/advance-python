class Logger:
    def __init__(self, filepath):
        self.file = open(filepath, "a")
        print("Logger started")

    def log(self, message, level="INFO"):
        self.file.write(f"{level}: {message}\n")

    def __del__(self):
        self.file.close()
        print("Logger closed")


# Example
logger = Logger("log.txt")

logger.log("This is an info message")
logger.log("This is a warning", "WARNING")
logger.log("This is an error", "ERROR")

del logger