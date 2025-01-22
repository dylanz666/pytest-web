from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tools.decorators import log_allure_step, screenshot_on_failure


class SearchPage(BasePage):
    # element locators
    SEARCH_INPUT_BOX = "todo-input"

    def __init__(self, driver):
        self.driver = driver

        super().__init__(self.driver)
        self.url = "https://todomvc.com/examples/react/dist/"

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
