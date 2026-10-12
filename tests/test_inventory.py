import pytest

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


@pytest.mark.smoke
def test_products_page_lists_six_items(logged_in):
    assert len(logged_in.product_names()) == 6


@pytest.mark.regression
def test_all_prices_are_positive(logged_in):
    assert all(price > 0 for price in logged_in.product_prices())


@pytest.mark.regression
@pytest.mark.parametrize("option, key, reverse", [
    ("name_asc", "names", False),
    ("name_desc", "names", True),
    ("price_asc", "prices", False),
    ("price_desc", "prices", True),
])
def test_sorting(logged_in, option, key, reverse):
    logged_in.sort_by(option)
    values = logged_in.product_names() if key == "names" else logged_in.product_prices()
    assert values == sorted(values, reverse=reverse)


@pytest.mark.smoke
def test_add_item_updates_cart_badge_and_button(logged_in):
    logged_in.add_to_cart(BACKPACK)
    assert logged_in.cart_count() == 1
    assert logged_in.button_text(BACKPACK) == "Remove"


@pytest.mark.regression
def test_remove_item_clears_cart_badge(logged_in):
    logged_in.add_to_cart(BACKPACK)
    logged_in.remove_from_cart(BACKPACK)
    assert logged_in.cart_count() == 0
    assert logged_in.button_text(BACKPACK) == "Add to cart"


@pytest.mark.regression
def test_cart_count_persists_after_refresh(logged_in, driver):
    logged_in.add_to_cart(BACKPACK)
    logged_in.add_to_cart(BIKE_LIGHT)
    driver.refresh()
    assert logged_in.cart_count() == 2
