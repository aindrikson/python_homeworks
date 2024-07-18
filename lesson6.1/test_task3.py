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

driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()

driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
driver.find_element(By.XPATH, "//button[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='Checkout']").click()

driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Александра")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Индриксон")
driver.find_element(By.XPATH, "//input[@placeholder='Zip/Postal Code']").send_keys("410018")

driver.find_element(By.XPATH, "//input[@id='continue']").click()
total = driver.find_element(By.XPATH, "//div[@class='summary_total_label']")
total_price = total.text.strip().replace("Total: $", "")

driver.quit()
def test_total():
    res = total_price
    assert res == "58.29"