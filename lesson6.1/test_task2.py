import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

driver.find_element(By.XPATH, "//input[@id='delay']").clear()
driver.find_element(By.XPATH, "//input[@id='delay']").send_keys("45")

driver.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='7']").click()
driver.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'operator') and normalize-space(.)='+']").click()
driver.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='8']").click()
driver.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='=']").click()

element = WebDriverWait (driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(concat(' ',@class,' '),'screen') and normalize-space(.)='15']"))
)

def test_rusult():
    assert "15" in driver.find_element(By.XPATH, "//div[contains(concat(' ',@class,' '),'screen') and normalize-space(.)='15']").text