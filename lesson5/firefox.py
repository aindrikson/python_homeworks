from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#Клик по кнопке
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
for x in range (1, 6):
    button.click()
sleep(10)
delete = driver.find_elements(By.XPATH, "//button[normalize-space(text())='Delete']")
print(len(delete))
sleep(10)

# #Клик по кнопке без ID
driver.get("http://uitestingplayground.com/dynamicid")
button = driver.find_element (By.XPATH, "//button[normalize-space(text())='Button with Dynamic ID']")
button.click()

#Клик по кнопке с CSS-классом
driver.get("http://uitestingplayground.com/classattr")
button = driver.find_element(By.XPATH, "//button[@class='btn class3 btn-primary btn-test']")
button.click()

#Модальное окно
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(10)
button = driver.find_element (By.XPATH, "//p[normalize-space(text())='Close']")
button.click()

# #Поле ввода
driver.get("http://the-internet.herokuapp.com/inputs")
search_input = driver.find_element (By.XPATH, "//input[@type='number']")
search_input.send_keys("1000")
search_input = driver.find_element (By.XPATH, "//input[@type='number']")
search_input.clear()
search_input = driver.find_element (By.XPATH, "//input[@type='number']")
search_input.send_keys("999")

# #Форма авторизации
driver.get("http://the-internet.herokuapp.com/login")
search_input = driver.find_element (By.XPATH, "//input[@id='username']")
search_input.send_keys("tomsmith")
search_input = driver.find_element (By.XPATH, "//input[@type='password']")
search_input.send_keys("SuperSecretPassword!")
button = driver.find_element (By.XPATH, "//i[normalize-space(text())='Login']")
button.click()