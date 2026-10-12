# SauceDemo QA Automation Framework

![UI Tests](https://github.com/divakars10/saucedemo-qa-automation/actions/workflows/tests.yml/badge.svg)

A UI test automation framework for the [SauceDemo](https://www.saucedemo.com) e-commerce site,
built with **Python, Selenium WebDriver and pytest** using the **Page Object Model (POM)**.

It covers login, product sorting, cart and checkout flows with **29 automated tests**,
and includes manual test cases and bug reports.

## Tech stack

| Area | Tool |
|------|------|
| Language | Python 3 |
| Browser automation | Selenium WebDriver 4 |
| Test runner | pytest (fixtures, parametrization, markers) |
| Reporting | pytest-html, screenshots on failure |
| Design pattern | Page Object Model |
| CI | GitHub Actions (headless Chrome) |

## Project structure

```
saucedemo-qa-automation/
├── pages/                  # Page Object classes (locators + actions)
│   ├── base_page.py        # Shared helpers with explicit waits
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                  # Test cases, grouped by feature
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── utils/config.py         # URL, timeouts, test data
├── docs/
│   ├── test_cases.md       # 31 manual test cases (29 automated)
│   └── bug_reports.md      # Defect reports
├── conftest.py             # Browser fixture, CLI options, screenshot hook
├── pytest.ini
└── .github/workflows/tests.yml
```

## What is tested

| Module | Coverage |
|--------|----------|
| Login | Valid login, locked-out user, wrong/empty credentials, case sensitivity, logout, direct URL access, back button after logout |
| Products | Product count, price validation, 4 sort options |
| Cart | Add/remove, badge count, persistence after refresh, continue shopping |
| Checkout | End-to-end purchase, total calculation, required-field validation, known defect (xfail) |

## How to run

```bash
# 1. Clone and set up
git clone https://github.com/divakars10/saucedemo-qa-automation.git
cd saucedemo-qa-automation
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt

# 2. Run all tests (Chrome must be installed; the driver downloads automatically)
pytest

# Other options
pytest --headless              # no browser window
pytest --browser firefox       # run on Firefox
pytest -m smoke                # only smoke tests
pytest -m regression           # only regression tests
pytest tests/test_login.py     # one file
pytest -n 4                    # parallel (needs: pip install pytest-xdist)
```

After a run, open `reports/report.html` in a browser. Screenshots of failed tests are saved
in `reports/screenshots/`.

## Key design decisions

- **Page Object Model:** Locators and page actions live in `pages/`, so tests read like
  user steps and a UI change only needs one fix.
- **Explicit waits only:** `BasePage` uses `WebDriverWait`, no `time.sleep()`, which keeps tests stable.
- **Data-driven tests:** `@pytest.mark.parametrize` runs one test with many inputs
  (e.g. 6 invalid-login cases in one function).
- **Fresh browser per test:** Each test gets its own driver, so tests don't depend on each other.
- **Known defects as `xfail`:** Bugs are tracked in `docs/bug_reports.md` and marked
  `xfail`, so the suite stays green while still documenting the issue.
