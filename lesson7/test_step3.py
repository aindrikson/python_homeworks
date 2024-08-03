from AuthorizationPage import Authorization
from AddPage import Add
from ShoppingCart import ShoppingCart
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
service=FirefoxService(GeckoDriverManager().install()))

def test_authorization():
    start=Authorization(driver)
    start.authorization()
    
    add_page = Add(driver)
    add_page.add_element()
    add_page.shopping_cart()

    shopping_cart_page = ShoppingCart(driver)
    shopping_cart_page.checkout()
    shopping_cart_page.fill_out_the_form()
    shopping_cart_page.total()


    