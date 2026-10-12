import pytest

from pages.login_page import LoginPage
from utils.config import BASE_URL, PASSWORD, USERS


@pytest.mark.smoke
def test_valid_login_opens_products_page(driver):
    inventory = LoginPage(driver).login(USERS["standard"], PASSWORD)
    assert inventory.title() == "Products"
    assert "inventory.html" in inventory.current_url


@pytest.mark.regression
@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
    ("standard_user", "wrong_password", "Username and password do not match"),
    ("unknown_user", "secret_sauce", "Username and password do not match"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("", "", "Username is required"),
], ids=["locked_out", "wrong_password", "unknown_user",
        "empty_username", "empty_password", "both_empty"])
def test_invalid_login_shows_error(driver, username, password, expected_error):
    login = LoginPage(driver)
    login.enter_credentials(username, password)
    assert expected_error in login.error_message()
    assert "inventory.html" not in login.current_url


@pytest.mark.regression
def test_password_is_case_sensitive(driver):
    login = LoginPage(driver)
    login.enter_credentials(USERS["standard"], PASSWORD.upper())
    assert "do not match" in login.error_message()


@pytest.mark.regression
def test_inventory_blocked_without_login(driver):
    driver.get(BASE_URL + "inventory.html")
    login = LoginPage(driver)
    assert login.is_displayed()
    assert "when you are logged in" in login.error_message()


@pytest.mark.smoke
def test_logout_returns_to_login_page(logged_in):
    login = logged_in.logout()
    assert login.is_displayed()


@pytest.mark.regression
def test_back_button_after_logout_does_not_restore_session(logged_in, driver):
    logged_in.logout()
    driver.back()
    # Protected page should redirect back to login
    driver.refresh()
    assert LoginPage(driver).is_displayed()
