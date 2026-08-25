import pytest
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from utils.test_data import PRODUCT_NAME


@pytest.mark.ui
class TestProducts:
    def test_products_list_visible(self, logged_in_page: ProductsPage):
        assert logged_in_page.is_loaded()
        assert logged_in_page.get_items_count() == 6

    def test_add_product_to_cart(self, logged_in_page: ProductsPage, cart_page: CartPage):
        logged_in_page.add_product(PRODUCT_NAME)

        assert logged_in_page.cart_badge.is_visible()
        assert logged_in_page.cart_badge.inner_text() == "1"

        logged_in_page.open_cart()
        assert PRODUCT_NAME in cart_page.get_item_names()