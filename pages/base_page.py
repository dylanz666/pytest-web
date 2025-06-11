from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from tools.config_util import ConfigUtil
from tools.decorators import allure_step


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, ConfigUtil.get_global_timeout())

    @allure_step
    def open_url(self, url):
        """打开 url"""
        self.driver.get(url)

    @allure_step
    def close(self):
        """关闭当前浏览器"""
        self.driver.quit()

    @allure_step
    def get_window_size(self):
        """获取页面尺寸"""
        window_size = self.driver.get_window_size()
        return window_size['width'], window_size['height']

    @allure_step
    def get_page_source(self):
        """获取页面的源代码"""
        return self.driver.page_source

    @allure_step
    def save_page_source(self, file_path):
        """获取页面的源代码并保存"""
        page_source = self.driver.page_source
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(page_source)

    @allure_step
    def get_title(self):
        """获取当前页面的标题"""
        return self.driver.title

    @allure_step
    def get_current_url(self):
        """获取当前页面的 URL"""
        return self.driver.current_url

    @allure_step
    def get_text(self, by, value):
        """获取元素文本"""
        return self.find_element(by, value).text

    @allure_step
    def get_attribute(self, by, value, attribute_name):
        """获取元素属性值"""
        return self.find_element(by, value).get_attribute(attribute_name)

    @allure_step
    def get_element_attributes(self, by, value):
        """获取元素的所有属性及其值"""
        element = self.find_element(by, value)
        return {attr.name: attr.value for attr in element.get_property('attributes')}

    @allure_step
    def get_css_value(self, by, value, css_property):
        """获取指定元素的 CSS 属性值"""
        element = self.find_element(by, value)
        return element.value_of_css_property(css_property)

    @allure_step
    def take_screenshot(self, file_path):
        """截取当前页面的屏幕截图并保存到指定路径"""
        self.driver.save_screenshot(file_path)

    @allure_step
    def click(self, by, value):
        """点击元素"""
        self.find_element(by, value).click()

    @allure_step
    def get_element_position(self, by, value):
        """获取元素在页面上的坐标"""
        return self.find_element(by, value).location

    @allure_step
    def click_position(self, x_coordinate, y_coordinate):
        """点击元素"""
        # way 1
        actions = ActionChains(self.driver)
        actions.move_by_offset(x_coordinate, y_coordinate).click().perform()
        # way 2
        # self.driver.execute_script(f"document.elementFromPoint({x_coordinate}, {y_coordinate}).click();")

    @allure_step
    def click_if_exists(self, by, value):
        """尝试点击元素，如果元素不存在则跳过"""
        try:
            self.find_element(by, value).click()
        except NoSuchElementException:
            pass

    @allure_step
    def find_element(self, by, value):
        """获取元素"""
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def _find_element(self, by, value):
        """获取元素"""
        return self.wait.until(EC.presence_of_element_located((by, value)))

    @allure_step
    def is_exists(self, by, value):
        try:
            self._find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    @allure_step
    def find_elements(self, by, value):
        """获取多个元素并返回它们的列表"""
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    @allure_step
    def wait_until_appears(self, by, value):
        """等待指定元素出现"""
        self.wait.until(EC.presence_of_element_located((by, value)))

    @allure_step
    def wait_until_disappears(self, by, value):
        """等待指定元素消失"""
        self.wait.until(EC.invisibility_of_element_located((by, value)))

    @allure_step
    def wait_until_clickable(self, by, value):
        """等待元素可点击"""
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    @allure_step
    def wait_until_text_present(self, by, value, text):
        """等待指定文本出现在元素中"""
        self.wait.until(EC.text_to_be_present_in_element((by, value), text))

    @allure_step
    def input(self, by, value, keys):
        """输入文本"""
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(keys)

    @allure_step
    def clear_input(self, by, value):
        """清除输入框中的文本"""
        element = self.find_element(by, value)
        element.clear()

    @allure_step
    def switch_to_iframe(self, by, value):
        """切换到指定的 iframe"""
        iframe = self.find_element(by, value)
        self.driver.switch_to.frame(iframe)

    @allure_step
    def switch_to_default_content(self):
        """从 iframe 返回到主文档"""
        self.driver.switch_to.default_content()

    @allure_step
    def select_dropdown_by_index(self, by, value, index):
        """通过索引选择下拉框中的选项"""
        element = self.find_element(by, value)
        select = Select(element)
        select.select_by_index(index)

    @allure_step
    def select_dropdown_by_visible_text(self, by, value, text):
        """通过可见文本选择下拉框中的选项"""
        element = self.find_element(by, value)
        select = Select(element)
        select.select_by_visible_text(text)

    @allure_step
    def select_dropdown_by_value(self, by, value, dropdown_value):
        """通过值选择下拉框中的选项"""
        element = self.find_element(by, value)
        select = Select(element)
        select.select_by_value(dropdown_value)

    @allure_step
    def scroll_to_element(self, by, value):
        """滚动到指定元素"""
        element = self.find_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure_step
    def open_new_tab(self, url):
        """打开新标签页并导航到指定 URL"""
        self.driver.execute_script("window.open(arguments[0], '_blank');", url)

    @allure_step
    def switch_to_tab(self, tab_index):
        """切换到指定的标签页"""
        tabs = self.driver.window_handles
        if tab_index < len(tabs):
            self.driver.switch_to.window(tabs[tab_index])
            return
        raise IndexError("Tab index out of range.")

    @allure_step
    def close_current_tab(self):
        """关闭当前标签页"""
        self.driver.close()
