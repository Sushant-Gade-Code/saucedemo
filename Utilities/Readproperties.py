import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\Admin\\saucedemo_project\\Configuration\\config.ini")

class ReadProperties:
    @staticmethod
    def getUrl():
        url=config.get("LogIn Info","url")
        return url

    @staticmethod
    def getUsername():
        userName=config.get("LogIn Info","UserName")
        return userName

    @staticmethod
    def getPassword():
        password = config.get("LogIn Info", "PassWord")
        return password
