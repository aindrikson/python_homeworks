from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    
    def add_value(self):
        self.driver.find_element(By.XPATH, "//input[@name='first-name']").send_keys("Иван")
        self.driver.find_element(By.XPATH, "//input[@name='last-name']").send_keys("Петров")
        self.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("Ленина, 55-3")
        self.driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Москва")
        self.driver.find_element(By.XPATH, "//input[@name='country']").send_keys("Россия")
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@skypro.com")
        self.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("+7985899998787")
        self.driver.find_element(By.XPATH, "//input[@name='job-position']").send_keys("QA")
        self.driver.find_element(By.XPATH, "//input[@name='company']").send_keys("SkyPro")
   
    def click_submit(self):
         self.driver.find_element(By.XPATH, "//button[contains(concat(' ',@class,' '),'btn') and normalize-space(.)='Submit']").click()

    def get_class_zip_code(self):
        return self.driver.find_element(By.XPATH, "//div[contains(concat(' ',@class,' '),'alert') and normalize-space(.)='N/A']").get_attribute("class")
     
    def get_class_first_name(self):
        return self.driver.find_element(By.XPATH, "//div[@id='first-name']").get_attribute("class")
    
    def get_class_last_name(self):
        return self.driver.find_element(By.XPATH, "//div[@id='last-name']").get_attribute("class")
    
    def get_class_adress(self):
        return self.driver.find_element(By.XPATH, "//div[@id='address']").get_attribute("class")
   
    def get_class_city(self):
        return self.driver.find_element(By.XPATH, "//div[@id='city']").get_attribute("class")
   
    def get_class_country(self):
        return self.driver.find_element(By.XPATH, "//div[@id='country']").get_attribute("class")
  
    def get_class_email(self):
        return self.driver.find_element(By.XPATH, "//div[@id='e-mail']").get_attribute("class")
   
    def get_class_phone(self):
        return self.driver.find_element(By.XPATH, "//div[@id='phone']").get_attribute("class")
   
    def get_class_job_position(self):
        return self.driver.find_element(By.XPATH, "//div[@id='job-position']").get_attribute("class")
   
    def get_class_company(self):
        return self.driver.find_element(By.XPATH, "//div[@id='company']").get_attribute("class")