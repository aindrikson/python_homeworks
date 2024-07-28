
from MainPage import MainPage
from ClassCheck import ClassCheck
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
def test_form():
    main_page = MainPage(driver)
    main_page.add_value()
    main_page.click_submit()

def test_class():
    class_check = ClassCheck(driver)
    class_check.get_class_zip_code()
    class_check.get_class_first_name()
    class_check.get_class_last_name()
    class_check.get_class_adress()
    class_check.get_class_city()
    class_check.get_class_country()
    class_check.get_class_email()
    class_check.get_class_phone()
    class_check.get_class_job_position()
    class_check.get_class_company()
    
    assert "danger" in class_check.get_class_zip_code()
    assert "success" in class_check.get_class_last_name()
    assert "success" in class_check.get_class_adress()
    assert "success" in class_check.get_class_city()
    assert "success" in class_check.get_class_country()
    assert "success" in class_check.get_class_email()
    assert "success" in class_check.get_class_phone()
    assert "success" in class_check.get_class_job_position()
    assert "success" in class_check.get_class_company()