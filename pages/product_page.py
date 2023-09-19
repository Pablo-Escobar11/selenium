from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_the_basket(self):
        self.browser.execute_script("window.scrollBy(0, 100);")
        self.browser.find_element(*ProductPageLocators.add_to_basket).click()

    def check_success_message(self):
        assert self.is_element_present(*ProductPageLocators.product_name), f"Отсутствует название продукта"
        assert self.is_element_present(*ProductPageLocators.message_about_adding), "осутствует сообщение о добавлении"
        self.product_name = self.browser.find_element(*ProductPageLocators.product_name).text
        message = self.browser.find_element(*ProductPageLocators.message_about_adding).text
        assert self.product_name in message, "Название продукта не совпадает с названием продукта в сообщении"

    def check_success_price_in_massage(self):
        msg_lst = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        assert product_price == msg_lst[2].text, "Wrong price product added to basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGES), "Сообщение появилось на страинце, после добавление в корзину"

    def message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Сообщение не исчезает"
