from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '[class="btn-group"] :nth-of-type(1)')


class BasketPageLocators():
    CHECK_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "[class='col-sm-6 h3']")
    MESSAGE_YOUR_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div#content_inner p")



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_SUCCESS_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages :nth-of-type(1) > .alertinner")
    NAME_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-of-type(1) > .alertinner strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    MESSAGE_PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages :nth-of-type(3) > .alertinner")

