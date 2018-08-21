from base.base_driver import init_driver
from page.display_page import DisplayPage
from page.first_network_type import FirstNetworkType
from page.more_page import MorePage
from page.setting import SettingPage
from page.mobile_network_page import MobileNetworkPage


class TestMore:

    def setup(self):
        self.driver = init_driver()
        self.setting_page = SettingPage(self.driver)
        self.more_page = MorePage(self.driver)
        self.first_network_type_page = FirstNetworkType(self.driver)
        self.mobile_network_page = MobileNetworkPage(self.driver)
        self.display_page = DisplayPage(self.driver)

    def test_network_2g(self):
        self.setting_page.click_more()
        self.more_page.click_mobile_network()
        self.mobile_network_page.click_first_network_type()
        self.first_network_type_page.click_2g_button()

    def test_network_3g(self):
        self.setting_page.click_more()
        self.more_page.click_mobile_network()
        self.mobile_network_page.click_first_network_type()
        self.first_network_type_page.click_3g_button()

