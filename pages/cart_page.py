from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def title(self):
        return self.text_of(self.TITLE)

    def item_names(self):
        if not self.is_present(self.ITEM_NAMES):
            return []
        return [e.text for e in self.driver.find_elements(*self.ITEM_NAMES)]

    def remove(self, product_name):
        self.click((By.XPATH,
                    f"//div[text()='{product_name}']"
                    f"/ancestor::div[@class='cart_item']//button"))

    def checkout(self):
        from pages.checkout_page import CheckoutPage
        self.click(self.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)

    def continue_shopping(self):
        from pages.inventory_page import InventoryPage
        self.click(self.CONTINUE_SHOPPING)
        return InventoryPage(self.driver)
