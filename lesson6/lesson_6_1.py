from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.implicitly_wait(20)
driver.get("http://www.uitestingplayground.com/ajax")
driver.find_element(By.XPATH, "//button[normalize-space(text())='Button Triggering AJAX Request']").click()
content = driver.find_element(By.XPATH, "//div[@id='content']")
txt = content.find_element(By.XPATH, "//p[normalize-space(text())='Data loaded with AJAX get request.']").text
print(txt)
driver.quit()