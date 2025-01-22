from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tools.decorators import log_allure_step, screenshot_on_failure


class HomePage(BasePage):
    # element locators
    LOGO = "//img[@class='logo'][@alt='TodoMVC']"
    SEARCH_PAGE_ENTRY = "//a[@href='examples/react/dist/']"

    def __init__(self, driver):
        self.driver = driver

        super().__init__(self.driver)
        self.url = "https://todomvc.com"

    @log_allure_step()
    @screenshot_on_failure()
    def open(self):
        self.open_url(self.url)

    @log_allure_step()
    @screenshot_on_failure()
    def is_opened(self):
        return self.is_exists(By.XPATH, self.LOGO)

    @log_allure_step()
    @screenshot_on_failure()
    def open_search_page(self):
        self.click(By.XPATH, self.SEARCH_PAGE_ENTRY)
