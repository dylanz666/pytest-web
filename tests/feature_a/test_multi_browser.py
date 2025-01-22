import pytest
import allure

from browsers.browser_factory import BrowserFactory
from constants.severity import Severity
from pages.home_page import HomePage
from pages.search_page import SearchPage
from tools.decorators import screenshot_at_the_end


@allure.feature("Feature: Demo multi browser")
class TestMultiBrowser:
    def setup_class(self):
        self.chrome_driver = BrowserFactory.create_browser().create_driver()
        self.home_page = HomePage(self.chrome_driver)

        self.edge_driver = BrowserFactory.create_browser("Edge").create_driver()
        self.home_page_on_edge = HomePage(self.edge_driver)

    def teardown_class(self):
        self.home_page.close()
        self.home_page_on_edge.close()

    def setup_method(self):
        self.home_page.open()
        assert self.home_page.is_opened()

    def teardown_method(self):
        pass

    @pytest.mark.P0
    @allure.severity(Severity.BLOCKER.value)
    @allure.title("Demo multi browser")
    @allure.description("Demo multi browser")
    @allure.testcase("https://platform/test/case?id=123")
    @screenshot_at_the_end(driver=lambda self: self.chrome_driver)
    @screenshot_at_the_end(driver=lambda self: self.edge_driver)
    # @pytest.mark.skip
    def test_multi_browser(self):
        # browser 1: chrome
        self.home_page.open_search_page()
        self.search_page = SearchPage(self.chrome_driver)
        assert self.search_page.is_opened()
        self.search_page.search("How to use pytest?")

        # browser 2: edge
        self.home_page_on_edge.open()
        assert self.home_page_on_edge.is_opened()
        self.home_page_on_edge.open_search_page()
        self.search_page_on_edge = SearchPage(self.edge_driver)
        assert self.search_page_on_edge.is_opened()
        self.search_page_on_edge.search("How to use python?")
