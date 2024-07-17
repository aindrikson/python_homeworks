from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
element = WebDriverWait (driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//img[@id='landscape']"))
)
get_src = driver.find_element(By.XPATH, "//img[@id='award']").get_attribute("src")
print(get_src)
driver.quit()