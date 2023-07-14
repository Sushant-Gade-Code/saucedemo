import inspect
import logging

class Loggen:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        File = logging.FileHandler("C:\\Users\\Admin\\saucedemo_project\\Logs\\Git.log")
        Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s :%(lineno)s: %(message)s")
        File.setFormatter(Formatter)
        logger.addHandler(File)
        logger.setLevel(logging.DEBUG)
        return logger