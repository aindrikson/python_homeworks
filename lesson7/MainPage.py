from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Value import *


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()
        self.driver.quit()
    
    def add_value(self):
        self.driver.find_element(By.XPATH, "//input[@name='first-name']").send_keys("first_name")
        self.driver.find_element(By.XPATH, "//input[@name='last-name']").send_keys("last_name")
        self.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("address")
        self.driver.find_element(By.XPATH, "//input[@name='city']").send_keys("city")
        self.driver.find_element(By.XPATH, "//input[@name='country']").send_keys("country")
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("email")
        self.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("phone")
        self.driver.find_element(By.XPATH, "//input[@name='job-position']").send_keys("job_position")
        self.driver.find_element(By.XPATH, "//input[@name='company']").send_keys("company")

    
    def click_submit(self):
         self.driver.find_element(By.XPATH, "//button[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='Submit']").click()

   