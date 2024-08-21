from CalcPage import Calc
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import allure

driver = webdriver.Firefox(
service=FirefoxService(GeckoDriverManager().install()))
@allure.epic("Calculator")
@allure.severity(severity_level='normal')
@allure.title("Работа калькулятора")
@allure.description("Поиск полей, ввод данных и вывод результата вычисления")
@allure.feature('Тест 2')
def test_calc():
 with allure.step("Открываем калькулятор, вводим значения и выполняем вычисление и ожидаем результат"):
    calc=Calc(driver)
    calc.time()
    calc.sum()
    calc.wait_res()
 with allure.step("Сравниваем полученный результат с ожидаемым"):
    calc.test_rusult()