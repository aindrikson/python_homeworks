
from MainPage import MainPage
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import allure

driver = webdriver.Firefox(
service=FirefoxService(GeckoDriverManager().install()))

@allure.epic("Data types")
@allure.severity(severity_level='normal')
@allure.title("Заполнение формы")
@allure.description("Заполняем форму данными и проверяем цвет поля Zip code")
@allure.feature('Тест 1')
def test_form():
 with allure.step("Открываем форму и заполняем ее данными, отправляем форму"):
    main_page = MainPage(driver)
    main_page.add_value()
    main_page.click_submit()
 with allure.step("Получаем значение классов полей"):
    main_page.get_class_zip_code()
    main_page.get_class_first_name()
    main_page.get_class_last_name()
    main_page.get_class_adress()
    main_page.get_class_city()
    main_page.get_class_country()
    main_page.get_class_email()
    main_page.get_class_phone()
    main_page.get_class_job_position()
    main_page.get_class_company()

 with allure.step("Проверяем значение классов полей"):
    assert "danger" in main_page.get_class_zip_code()
    assert "success" in main_page.get_class_last_name()
    assert "success" in main_page.get_class_adress()
    assert "success" in main_page.get_class_city()
    assert "success" in main_page.get_class_country()
    assert "success" in main_page.get_class_email()
    assert "success" in main_page.get_class_phone()
    assert "success" in main_page.get_class_job_position()
    assert "success" in main_page.get_class_company()