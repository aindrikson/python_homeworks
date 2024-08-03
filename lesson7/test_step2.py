from CalcPage import Calc
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(
service=FirefoxService(GeckoDriverManager().install()))

def test_calc():
    calc=Calc(driver)
    calc.time()
    calc.sum()
    calc.wait_res()
    calc.test_rusult()