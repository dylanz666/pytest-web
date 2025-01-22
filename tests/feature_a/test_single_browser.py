import pytest
import allure

from browsers.browser_factory import BrowserFactory
from constants.severity import Severity
from pages.home_page import HomePage
from pages.search_page import SearchPage
from tools.decorators import screenshot_on_failure


@allure.feature("Feature: Demo single browser")
class TestMultiBrowser:
    def setup_class(self):
        self.driver = BrowserFactory.create_browser().create_driver()
        self.home_page = HomePage(self.driver)

    def teardown_class(self):
        self.home_page.close()

    def setup_method(self):
        self.home_page.open()
        assert self.home_page.is_opened()

    def teardown_method(self):
        pass

    @pytest.mark.P1
    @allure.severity(Severity.CRITICAL.value)
    @allure.title("Demo single browser")
    @allure.description("Demo single browser")
    @allure.testcase("https://platform/test/case?id=124")
    @screenshot_on_failure()
    # @pytest.mark.skip
    def test_single_browser(self):
        self.home_page.open_search_page()
        self.search_page = SearchPage(self.driver)
        assert self.search_page.is_opened()
        self.search_page.search("How to use python?")
