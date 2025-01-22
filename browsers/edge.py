from selenium import webdriver
from selenium.webdriver.chrome.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from browsers.browser import Browser
from tools.config_util import ConfigUtil


class Edge(Browser):
    def create_driver(self):
        options = webdriver.EdgeOptions()
        # 解决某些环境下的安全问题
        options.add_argument("--no-sandbox")
        # 无头模式（可选）
        # options.add_argument("--headless")
        # 禁用 GPU 加速
        # options.add_argument("--disable-gpu")

        selenium_server = ConfigUtil.get_selenium_server()
        selenium_server = selenium_server if selenium_server else None
        if selenium_server is None:
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        return webdriver.Remote(command_executor=selenium_server, options=options)
