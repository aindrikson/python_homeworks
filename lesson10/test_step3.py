from AuthorizationPage import Authorization
from AddPage import Add
from ShoppingCart import ShoppingCart
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import allure

driver = webdriver.Firefox(
service=FirefoxService(GeckoDriverManager().install()))

@allure.epic("Swag Labs")
@allure.severity(severity_level='normal')
@allure.title("Покупка и офрмление товаров")
@allure.description("Добавляем необходимые вещи в корзину, заполняем форму для доставки и проверяем конечную сумму заказа")
@allure.feature('Тест 3')

def test_authorization():
 with allure.step("Авторизация на сайте"):
    start=Authorization(driver)
    start.authorization()

 with allure.step("Добавление элементов в корзину и переход в корзину"):
    add_page = Add(driver)
    add_page.add_element()
    add_page.shopping_cart()

# with allure.step("Заполнение формы доставки и проверка итоговой суммы заказа"):
#     shopping_cart_page = ShoppingCart(driver)
#     shopping_cart_page.checkout()
#     shopping_cart_page.fill_out_the_form()
#     shopping_cart_page.total()


    