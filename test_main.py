from time import sleep
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    browser.get(link)
    page.open()
    page.go_to_login_page()
    sleep(3)


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page_login = page.go_to_login_page()
    page_login.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser=browser, url=link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.there_is_no_products_in_basket()
    basket_page.check_text_about_empty_basket()

