from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from browsers.browser import Browser
from tools.config_util import ConfigUtil


class Chrome(Browser):
    def create_driver(self):
        options = webdriver.ChromeOptions()
        # 添加一些选项
        # 启动时最大化窗口
        options.add_argument("--start-maximized")
        # 禁用信息栏
        options.add_argument("--disable-infobars")
        # 无头模式（可选）
        # options.add_argument("--headless")

        selenium_server = ConfigUtil.get_selenium_server()
        selenium_server = selenium_server if selenium_server else None
        if selenium_server is None:
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        return webdriver.Remote(command_executor=selenium_server, options=options)
