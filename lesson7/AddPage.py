from selenium.webdriver.common.by import By

class Add:
    def __init__(self, driver):
        self.driver = driver
    
    def add_element(self):
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()
    
    def shopping_cart(self):
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()