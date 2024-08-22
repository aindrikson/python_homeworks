from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import allure

class Calc:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    @allure.step("Очищаем поле ввода и вводим новое значение")
    def time(self):
        self.driver.find_element(By.XPATH, "//input[@id='delay']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='delay']").send_keys("45")
    @allure.step("Производим вычисления")
    def sum(self):
        self.driver.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='7']").click()
        self.driver.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'operator') and normalize-space(.)='+']").click()
        self.driver.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='8']").click()
        self.driver.find_element(By.XPATH, "//span[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='=']").click()

    @allure.step("Ожидание результата вычисления")
    def wait_res(self):
        WebDriverWait (self.driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(concat(' ',@class,' '),'screen') and normalize-space(.)='15']"))
        )

    @allure.step("Получаем результат вычисления")
    def test_rusult(self):
        assert "15" in self.driver.find_element(By.XPATH, "//div[contains(concat(' ',@class,' '),'screen') and normalize-space(.)='15']").text