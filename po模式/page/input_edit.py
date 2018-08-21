from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class InputEdit(BaseAction):
    search_edit_text = By.CLASS_NAME, "android.widget.EditText"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def input_search(self, text):
        self.input(self.search_edit_text, text)

    def click_back(self):
        self.click(self.back_button)
