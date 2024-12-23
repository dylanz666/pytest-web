from selenium import webdriver
from browsers.browser import Browser


class Safari(Browser):
    def create_driver(self):
        options = webdriver.SafariOptions()
        return webdriver.Safari(options=options)
