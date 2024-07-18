import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.find_element(By.XPATH, "//input[@name='first-name']").send_keys("Иван")
driver.find_element(By.XPATH, "//input[@name='last-name']").send_keys("Петров")
driver.find_element(By.XPATH, "//input[@name='address']").send_keys("Ленина, 55-3")
driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Москва")
driver.find_element(By.XPATH, "//input[@name='country']").send_keys("Россия")
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@skypro.com")
driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("+7985899998787")
driver.find_element(By.XPATH, "//input[@name='job-position']").send_keys("QA")
driver.find_element(By.XPATH, "//input[@name='company']").send_keys("SkyPro")

driver.find_element(By.XPATH, "//button[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='Submit']").click()
sleep(5)

def test_form_danger():
    assert "danger" in driver.find_element(By.XPATH, "//div[contains(concat(' ',@class,' '),'alert') and normalize-space(.)='N/A']").get_attribute("class")

def test_form_success():
    assert "success" in driver.find_element(By.XPATH, "//div[@id='first-name']").get_attribute("class")
    assert "success" in driver.find_element(By.XPATH, "//div[@id='last-name']").get_attribute("class")
    assert "success" in driver.find_element(By.XPATH, "//div[@id='address']").get_attribute("class")
    assert "success" in driver.find_element(By.XPATH, "//div[@id='city']").get_attribute("class")
    assert "success" in driver.find_element(By.XPATH, "//div[@id='country']").get_attribute("class")
    assert "success" in driver.find_element(By.XPATH, "//div[@id='e-mail']").get_attribute("class")
    assert "success" in driver.find_element(By.XPATH, "//div[@id='phone']").get_attribute("class")
    assert "success" in driver.find_element(By.XPATH, "//div[@id='job-position']").get_attribute("class")
    assert "success" in driver.find_element(By.XPATH, "//div[@id='company']").get_attribute("class")