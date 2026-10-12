from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def enter_credentials(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Log in and return the inventory page (use for valid users)."""
        from pages.inventory_page import InventoryPage
        self.enter_credentials(username, password)
        return InventoryPage(self.driver)

    def error_message(self):
        return self.text_of(self.ERROR)

    def is_displayed(self):
        return self.find(self.LOGIN_BUTTON).is_displayed()
