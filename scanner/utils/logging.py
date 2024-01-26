import logging
import sys

from scanner.utils.singleton import Singleton


class Logger(object, metaclass=Singleton):
    """
    A singleton logger class for managing application logs.

    Attributes:
        rootLogger (logging.Logger): The root logger instance.

    Methods:
        __init__(): Initializes the logger with default settings.
        setRootLogLevel(level): Sets the log level for the root logger.
        getLogger(name): Retrieves a logger with the specified name.
    """

    rootLogger = None

    def __init__(self):
        """
        Initializes the logger with default settings.

        The logger is configured with a stream handler (console output) and a file handler (logs file).
        Default log level is set to INFO.
        """
        self.rootLogger = logging.getLogger()
        self.rootLogger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "{asctime} - {levelname:>3.3} - {name:>16.16} - {message}", style="{"
        )
        streamHandler = logging.StreamHandler(sys.stdout)
        streamHandler.setFormatter(formatter)

        fileHandler = logging.FileHandler("cleavercheat.log")
        fileHandler.setFormatter(formatter)

        self.rootLogger.addHandler(streamHandler)
        self.rootLogger.addHandler(fileHandler)

    def setRootLogLevel(self, level):
        """
        Set the log level for the root logger.

        Args:
            level (int): The logging level to be set.
        """
        self.rootLogger.setLevel(level)

    def getLogger(self, name):
        """
        Retrieve a logger with the specified name.

        Args:
            name (str): The name of the logger.

        Returns:
            logging.Logger: The logger instance.
        """
        return logging.getLogger(name)


logger = Logger()


def LoggerManager(logName):
    """
    Convenience function to retrieve a logger instance with the specified name.

    Args:
        logName (str): The name of the logger.

    Returns:
        logging.Logger: The logger instance.
    """
    return logger.getLogger(logName)
