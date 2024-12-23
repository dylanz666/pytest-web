from selenium.webdriver.common.by import By

from browsers.browser_factory import BrowserFactory
from pages.base_page import BasePage
from utils.config_util import ConfigUtil
from utils.decorators import log_allure_step, screenshot_on_failure


class HomePage(BasePage):
    # element locators
    SEARCH_INPUT_BOX = "kw"

    def __init__(self, browser_name=None):
        browser_name = browser_name if browser_name is not None else ConfigUtil.get_browser_name()
        browser = BrowserFactory.create_browser(browser_name)
        self.driver = browser.create_driver()

        super().__init__(self.driver)
        self.url = "https://www.baidu.com"

    @log_allure_step()
    @screenshot_on_failure()
    def open(self):
        self.open_url(self.url)

    @log_allure_step()
    @screenshot_on_failure()
    def is_opened(self):
        return self.is_exists(By.ID, self.SEARCH_INPUT_BOX)

    @log_allure_step()
    @screenshot_on_failure()
    def search(self, question_text):
        self.input(By.ID, self.SEARCH_INPUT_BOX, question_text)
