from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def check_text_about_empty_basket(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Basket')]")))
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET), "Корзина не пуста, в корзине присутствуют товары"

    def there_is_no_products_in_basket(self):
        product_in_basket = self.browser.find_elements(*BasketPageLocators.ELEMENTS_IN_BASKET)
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Basket')]")))
        assert len(product_in_basket) == 0, "В корзине присутствуют товары, она не пуста"
