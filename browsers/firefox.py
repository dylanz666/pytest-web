from selenium import webdriver
from selenium.webdriver.chrome.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from browsers.browser import Browser
from tools.config_util import ConfigUtil


class Firefox(Browser):
    def create_driver(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--disable-extensions')

        selenium_server = ConfigUtil.get_selenium_server()
        selenium_server = selenium_server if selenium_server else None
        if selenium_server is None:
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        return webdriver.Remote(command_executor=selenium_server, options=options)
