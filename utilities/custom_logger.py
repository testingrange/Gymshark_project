import logging
import inspect
import os

def cutomLogger(logLevel=logging.DEBUG, logName="automation"):
    loggerName = inspect.stack()[1][3]

    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(str(logName)+".log", mode="a")
    fileHandler.setLevel(logLevel)

    formatter = ""

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger