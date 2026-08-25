import pytest
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from utils.test_data import PRODUCT_NAME


@pytest.mark.ui
class TestCart:
    def test_remove_product_from_cart(self, logged_in_page: ProductsPage, cart_page: CartPage):
        logged_in_page.add_product(PRODUCT_NAME)
        logged_in_page.open_cart()

        assert not cart_page.is_empty()

        logged_in_page.open()
        logged_in_page.remove_product(PRODUCT_NAME)

        assert logged_in_page.cart_badge.count() == 0

    def test_checkout_negative_no_items(self, logged_in_page: ProductsPage, cart_page: CartPage):
        logged_in_page.open_cart()
        assert cart_page.is_empty()