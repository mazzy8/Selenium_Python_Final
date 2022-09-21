from .locators import ProductLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductLocators.ADD_TO_BASKET)
        button.click()
        self.should_be_message_add_product_to_basket()
        self.check_name_product_in_message_add_in_basket()
        self.should_be_message_price_basket()
        self.check_price_product_in_basket()

    def should_be_message_add_product_to_basket(self):
        text_message = self.browser.find_element(*ProductLocators.ALERT_SUCCESS_ADD_TO_BASKET).text
        assert "has been added" in text_message, "Wrong alert add product to basket"

    def check_name_product_in_message_add_in_basket(self):
        text_message = self.browser.find_element(*ProductLocators.ALERT_SUCCESS_ADD_TO_BASKET).text
        name_product = self.browser.find_element(*ProductLocators.NAME_PRODUCT).text
        assert name_product in text_message, "Wrong name product in alert add to basket"

    def should_be_message_price_basket(self):
        text_message = self.browser.find_element(*ProductLocators.ALERT_PRICE_PRODUCT_IN_BASKET).text
        assert 'total is now' in text_message, "Wrong message basket total in alert add to basket"

    def check_price_product_in_basket(self):
        text_message = self.browser.find_element(*ProductLocators.ALERT_PRICE_PRODUCT_IN_BASKET).text
        price_product = self.browser.find_element(*ProductLocators.PRICE_PRODUCT).text
        assert price_product[1:] in text_message, "Wrong price product in basket"
