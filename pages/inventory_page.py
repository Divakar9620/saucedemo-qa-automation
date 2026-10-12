from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    SORT_OPTIONS = {
        "name_asc": "az",
        "name_desc": "za",
        "price_asc": "lohi",
        "price_desc": "hilo",
    }

    @staticmethod
    def _item_button(product_name):
        return (By.XPATH,
                f"(//div[text()='{product_name}']"
                f"/ancestor::div[@class='inventory_item']//button)[1]")

    def title(self):
        return self.text_of(self.TITLE)

    def product_names(self):
        return [e.text for e in self.find_all(self.ITEM_NAMES)]

    def product_prices(self):
        return [float(e.text.replace("$", "")) for e in self.find_all(self.ITEM_PRICES)]

    def sort_by(self, option):
        Select(self.find(self.SORT_DROPDOWN)).select_by_value(self.SORT_OPTIONS[option])

    def add_to_cart(self, product_name):
        self.click(self._item_button(product_name))

    def remove_from_cart(self, product_name):
        self.click(self._item_button(product_name))

    def button_text(self, product_name):
        return self.text_of(self._item_button(product_name))

    def cart_count(self):
        if not self.is_present(self.CART_BADGE):
            return 0
        return int(self.text_of(self.CART_BADGE))

    def open_cart(self):
        from pages.cart_page import CartPage
        # Scroll to top so the cart icon is in view (it is not sticky on SauceDemo),
        # then confirm the page actually navigated before returning.
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.click(self.CART_LINK)
        self.wait.until(lambda d: "cart.html" in d.current_url)
        return CartPage(self.driver)

    def logout(self):
        from pages.login_page import LoginPage
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
        return LoginPage(self.driver)
