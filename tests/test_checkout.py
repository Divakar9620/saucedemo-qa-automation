import pytest

from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from utils.config import CHECKOUT_INFO, PASSWORD, USERS

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


@pytest.fixture
def checkout(logged_in):
    """Cart with two items, sitting on checkout step one."""
    logged_in.add_to_cart(BACKPACK)
    logged_in.add_to_cart(BIKE_LIGHT)
    return logged_in.open_cart().checkout()


@pytest.mark.smoke
def test_end_to_end_purchase(checkout):
    checkout.fill_information(**CHECKOUT_INFO)
    checkout.continue_to_overview()
    checkout.finish()
    assert checkout.confirmation_header() == "Thank you for your order!"


@pytest.mark.regression
def test_order_total_is_calculated_correctly(checkout):
    checkout.fill_information(**CHECKOUT_INFO)
    checkout.continue_to_overview()
    assert checkout.subtotal() == pytest.approx(sum(checkout.item_prices()))
    assert checkout.total() == pytest.approx(checkout.subtotal() + checkout.tax())


@pytest.mark.regression
@pytest.mark.parametrize("first, last, postal, expected_error", [
    ("", "S", "560001", "First Name is required"),
    ("Divakar", "", "560001", "Last Name is required"),
    ("Divakar", "S", "", "Postal Code is required"),
], ids=["missing_first_name", "missing_last_name", "missing_postal_code"])
def test_checkout_required_fields(checkout, first, last, postal, expected_error):
    checkout.fill_information(first, last, postal)
    checkout.continue_to_overview()
    assert expected_error in checkout.error_message()


@pytest.mark.regression
@pytest.mark.xfail(reason="Known defect BUG-001: problem_user cannot enter a last name "
                          "(see docs/bug_reports.md)", strict=False)
def test_problem_user_can_enter_last_name(driver):
    inventory = LoginPage(driver).login(USERS["problem"], PASSWORD)
    inventory.add_to_cart(BACKPACK)
    checkout = inventory.open_cart().checkout()
    checkout.fill_information(**CHECKOUT_INFO)
    assert checkout.field_value(CheckoutPage.LAST_NAME) == CHECKOUT_INFO["last_name"]
