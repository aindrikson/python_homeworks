from selenium.webdriver.common.by import By
import allure

class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")
    
    @allure.step("Переход к заполнению формы доставки")
    def checkout(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space(text())='Checkout']").click()

    @allure.step("Заполнение формы для доставки")
    def fill_out_the_form(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Александра")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Индриксон")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Zip/Postal Code']").send_keys("410018")
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()

    @allure.step("Проверка итоговой суммы доставки")
    def total(self):
        total = self.driver.find_element(By.XPATH, "//div[@class='summary_total_label']")
        total_price = total.text.strip().replace("Total: $", "")
        
        
        res = total_price
        assert res == "58.29"
        self.driver.quit()