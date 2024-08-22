from selenium.webdriver.common.by import By
import allure
class Authorization:
        def __init__(self, driver):
            self.driver = driver
            self.driver.get("https://www.saucedemo.com")
            self.driver.maximize_window()
            self.driver.implicitly_wait(4)

        @allure.step("Авторизация на сайте")
        def authorization(self):
            self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("standard_user")
            self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("secret_sauce")
            self.driver.find_element(By.XPATH, "//input[@type='submit']").click()