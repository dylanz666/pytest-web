from browsers.chrome import Chrome
from browsers.edge import Edge
from browsers.firefox import Firefox
from browsers.safari import Safari
from constants.browser_type import BrowserType
from tools.config_util import ConfigUtil


class BrowserFactory:
    @staticmethod
    def create_browser(browser_type=None):
        browser_type = browser_type if browser_type is not None else ConfigUtil.get_browser_name()
        if browser_type == BrowserType.CHROME.value:
            return Chrome()
        if browser_type == BrowserType.EDGE.value:
            return Edge()
        if browser_type == BrowserType.FIREFOX.value:
            return Firefox()
        if browser_type == BrowserType.SAFARI.value:
            return Safari()
        raise ValueError(f"Unknown browser type: {browser_type}")
