from configparser import ConfigParser

config = ConfigParser()
config.read(r'C:\Users\99455\Desktop\Automation\Selenium\floward_com\configurations\config.ini')


class ReadConfig:

    @staticmethod
    def get_url():
        url = config['common info']['main_url']
        return url

