from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def check_add_product_to_basket(self):
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_message_add_product_to_basket()
        self.check_name_product_in_message_add_in_basket()
        self.should_be_message_price_basket()
        self.check_price_product_in_basket()

    def should_be_message_add_product_to_basket(self):
        text_message = self.return_text_from_element_on_page(*ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET)
        assert "has been added to your basket." in text_message, "Wrong alert add product to basket"

    def check_name_product_in_message_add_in_basket(self):
        name_message = self.return_text_from_element_on_page(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE)
        name_product = self.return_text_from_element_on_page(*ProductPageLocators.NAME_PRODUCT)
        assert name_product == name_message, "Wrong name product in alert add to basket"

    def should_be_message_price_basket(self):
        text_message = self.return_text_from_element_on_page(*ProductPageLocators.MESSAGE_PRICE_PRODUCT_IN_BASKET)
        assert 'total is now' in text_message, "Wrong message basket total in alert add to basket"

    def check_price_product_in_basket(self):
        text_message = self.return_text_from_element_on_page(*ProductPageLocators.MESSAGE_PRICE_PRODUCT_IN_BASKET)
        price_product = self.return_text_from_element_on_page(*ProductPageLocators.PRICE_PRODUCT)
        assert price_product[1:] in text_message, "Wrong price product in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS_ADD_TO_BASKET), \
            "Success message is presented, but should not be"
