import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_AdminURL():
        url=config.get('admin login info','admin_page_url')
        return url
    @staticmethod
    def get_userName():
        userName=config.get('admin login info','userName')
        return userName

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_invaliduserName():
        invalid_userName=config.get('admin login info','invalid_userName')
        return invalid_userName















