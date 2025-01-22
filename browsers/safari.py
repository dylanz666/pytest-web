from selenium import webdriver
from browsers.browser import Browser
from tools.config_util import ConfigUtil


class Safari(Browser):
    def create_driver(self):
        options = webdriver.SafariOptions()

        selenium_server = ConfigUtil.get_selenium_server()
        selenium_server = selenium_server if selenium_server else None
        if selenium_server is None:
            return webdriver.Safari(options=options)
        return webdriver.Remote(command_executor=selenium_server, options=options)
