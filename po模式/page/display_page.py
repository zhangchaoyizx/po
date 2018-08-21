from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class DisplayPage(BaseAction):

    search_button = By.XPATH, "//*[@content-desc='搜索']"

    def click_search(self):
        self.click(self.search_button)
