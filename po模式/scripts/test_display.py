from page.setting import SettingPage
from page.display_page import DisplayPage
from page.input_edit import InputEdit
from base.base_driver import init_driver


class TestDisplay:
    def setup(self):
        self.driver = init_driver()
        self.setting_page = SettingPage(self.driver)
        self.display_page = DisplayPage(self.driver)
        self.input_edit = InputEdit(self.driver)

    def test_display_search(self):
        # 点击显示
        self.setting_page.click_display()
        # 点击放大镜
        self.display_page.click_search()
        # 搜索框输入文字
        self.input_edit.input_search("hello")
        # 点击返回
        self.input_edit.click_back()
