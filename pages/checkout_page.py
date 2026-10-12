from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Step one: your information
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    # Step two: overview
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH = (By.ID, "finish")

    # Complete
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME = (By.ID, "back-to-products")

    def fill_information(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)

    def field_value(self, locator):
        return self.find(locator).get_attribute("value")

    def continue_to_overview(self):
        self.click(self.CONTINUE)

    def error_message(self):
        return self.text_of(self.ERROR)

    @staticmethod
    def _amount(label_text):
        # "Item total: $29.99" -> 29.99
        return float(label_text.split("$")[-1])

    def item_prices(self):
        return [float(e.text.replace("$", "")) for e in self.find_all(self.ITEM_PRICES)]

    def subtotal(self):
        return self._amount(self.text_of(self.SUBTOTAL))

    def tax(self):
        return self._amount(self.text_of(self.TAX))

    def total(self):
        return self._amount(self.text_of(self.TOTAL))

    def finish(self):
        self.click(self.FINISH)

    def confirmation_header(self):
        return self.text_of(self.COMPLETE_HEADER)
