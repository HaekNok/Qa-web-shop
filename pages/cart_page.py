from playwright.sync_api import Page
from utils.test_data import BASE_URL


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.item_titles = page.locator(".inventory_item_name")
        self.checkout_btn = page.locator("#checkout")

    def open(self):
        self.page.goto(f"{BASE_URL}/cart.html")
        return self

    def is_empty(self) -> bool:
        return self.cart_items.count() == 0

    def get_item_names(self) -> list[str]:
        return self.item_titles.all_inner_texts()

    def proceed_to_checkout(self):
        self.checkout_btn.click()