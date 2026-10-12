import pytest

BACKPACK = "Sauce Labs Backpack"
ONESIE = "Sauce Labs Onesie"


@pytest.mark.smoke
def test_added_items_appear_in_cart(logged_in):
    logged_in.add_to_cart(BACKPACK)
    logged_in.add_to_cart(ONESIE)
    cart = logged_in.open_cart()
    assert cart.title() == "Your Cart"
    assert sorted(cart.item_names()) == sorted([BACKPACK, ONESIE])


@pytest.mark.regression
def test_remove_item_from_cart_page(logged_in):
    logged_in.add_to_cart(BACKPACK)
    cart = logged_in.open_cart()
    cart.remove(BACKPACK)
    assert cart.item_names() == []


@pytest.mark.regression
def test_continue_shopping_keeps_cart(logged_in):
    logged_in.add_to_cart(BACKPACK)
    inventory = logged_in.open_cart().continue_shopping()
    assert inventory.title() == "Products"
    assert inventory.cart_count() == 1
