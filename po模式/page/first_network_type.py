from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class FirstNetworkType(BaseAction):
    network_2g_button = By.XPATH, "//*[@text='2G']"
    network_3g_button = By.XPATH, "//*[@text='3G']"

    def click_2g_button(self):
        self.click(self.network_2g_button)

    def click_3g_button(self):
        self.click(self.network_3g_button)
