from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM_LOCATOR = (By.ID, "login_form")
    REGISTER_FORM_LOCATOR = (By.ID, "register_form")
    EMAIL_LOCATOR = (By.NAME, "registration-email")
    PASSWORD_LOCATOR = (By.NAME, "registration-password1")
    ACCEPT_PASSWORD_LOCATOR = (By.NAME, "registration-password2")


class ProductPageLocators:
    add_to_basket = (By.XPATH, "//button[@value = 'Добавить в корзину']")
    product_name = (By.CSS_SELECTOR, "div.product_main h1")
    message_about_adding = (By.CSS_SELECTOR, "div.alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")


class BasketPageLocators:
    TEXT_ABOUT_EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'empty')]")
    BASKET_LINK = (By.XPATH, "//a[contains(text(), 'View basket')]")
    ELEMENTS_IN_BASKET = (By.CLASS_NAME, "basket-items")
    BASKET_TEXT = (By.XPATH, "//h1[contains(text(), 'Basket')]")
