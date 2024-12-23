import time

import pytest
import allure
from constants.severity import Severity
from pages.home_page import HomePage
from utils.decorators import screenshot_at_the_end, screenshot_on_failure


@allure.feature("Feature: Test baidu on Chrome")
class TestBrowserDemo:
    def setup_class(self):
        self.home_page = HomePage()
        self.driver = self.home_page.driver

    def teardown_class(self):
        self.home_page.close()

    def setup_method(self):
        self.home_page.open()
        assert self.home_page.is_opened() is True
        time.sleep(2)

    def teardown_method(self):
        pass

    @pytest.mark.P0
    @allure.severity(Severity.BLOCKER.value)
    @allure.title("Demo search on baidu")
    @allure.description("Demo search on baidu")
    @allure.testcase("https://platform/test/case?id=123")
    @screenshot_on_failure()
    # @pytest.mark.skip
    def test_search_on_baidu(self):
        self.home_page.search("How to use pytest?")
        time.sleep(3)

    @pytest.mark.P1
    @allure.severity(Severity.CRITICAL.value)
    @allure.title("Demo search again on baidu")
    @allure.description("Demo search again on baidu")
    @allure.testcase("https://platform/test/case?id=124")
    @screenshot_at_the_end()
    # @pytest.mark.skip
    def test_search_again_on_baidu(self):
        self.home_page.search("How to use python?")
        time.sleep(3)
