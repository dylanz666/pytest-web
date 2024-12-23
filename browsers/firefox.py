from selenium import webdriver
from selenium.webdriver.chrome.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from browsers.browser import Browser


class Firefox(Browser):
    def create_driver(self):
        options = webdriver.EdgeOptions()
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
