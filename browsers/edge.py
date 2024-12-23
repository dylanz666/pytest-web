from selenium import webdriver
from selenium.webdriver.chrome.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from browsers.browser import Browser


class Edge(Browser):
    def create_driver(self):
        options = webdriver.EdgeOptions()
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
