import os
from datetime import datetime

import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from utils.config import BASE_URL, PASSWORD, USERS


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome or firefox")
    parser.addoption("--headless", action="store_true", help="run browser without a window")


def _chrome(headless):
    options = webdriver.ChromeOptions()
    # Stop Chrome's password-manager popups, which block clicks on saucedemo
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    options.add_argument("--incognito")
    options.add_argument("--window-size=1366,768")
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def _firefox(headless):
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument("-headless")
    return webdriver.Firefox(options=options)


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    # Selenium Manager (Selenium 4.6+) downloads the right driver automatically
    drv = _firefox(headless) if browser == "firefox" else _chrome(headless)
    drv.get(BASE_URL)
    yield drv
    drv.quit()


@pytest.fixture
def logged_in(driver):
    """Returns the InventoryPage after logging in as standard_user."""
    return LoginPage(driver).login(USERS["standard"], PASSWORD)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot whenever a test fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed and "driver" in item.fixturenames:
        drv = item.funcargs["driver"]
        os.makedirs("reports/screenshots", exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        drv.save_screenshot(f"reports/screenshots/{item.name}_{stamp}.png")
