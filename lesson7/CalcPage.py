from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
class Calc:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.browser.get = ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def time(self):
        self.browser.find_element(By.XPATH, "//input[@id='delay']").clear()
        self.browser.find_element(By.XPATH, "//input[@id='delay']").send_keys("45")

    def sum(self):
        self.browser.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='7']").click()
        self.browser.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'operator') and normalize-space(.)='+']").click()
        self.browser.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='8']").click()
        self.browser.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='=']").click()

    def wait_res(self):
        WebDriverWait (self.browser, 50).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(concat(' ',@class,' '),'screen') and normalize-space(.)='15']"))
        )
    
    def test_rusult(self):
        assert "15" in self.browser.find_element(By.XPATH, "//div[contains(concat(' ',@class,' '),'screen') and normalize-space(.)='15']").text