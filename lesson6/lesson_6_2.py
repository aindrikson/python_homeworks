from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("SkyPro")
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
button_name = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").text
print(button_name)
driver.quit()
