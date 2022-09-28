from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECK_PRODUCT_IN_BASKET), "Basket have product"

    def should_be_message_empty_basket(self):
        text = self.return_text_from_element_on_page(*BasketPageLocators.MESSAGE_YOUR_BASKET_IS_EMPTY)
        assert "Your basket is empty" == text.split('.')[0], f"{text} is not Your basket is empty"
