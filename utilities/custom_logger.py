import logging
import inspect

def customLogger(logLevel=logging.DEBUG, logName="automation"):

    logger = logging.getLogger(inspect.stack()[1][3])
    logger.setLevel(logLevel)

    fileHandler = logging.FileHandler(str(logName) + ".log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter("%(asctime)s- %(name)s- %(levelname)s- %(message)s", datefmt="%m/%d/%Y %H:%M:%S")

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger