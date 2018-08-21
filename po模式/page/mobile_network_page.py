from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MobileNetworkPage(BaseAction):
    first_network_type_button = By.XPATH, "//*[@text='首选网络类型']"

    def click_first_network_type(self):
        self.click(self.first_network_type_button)
