from selenium.webdriver.common.by import By



class ClassCheck:
    
    
    def __init__(self, driver):
        self.driver = driver
    
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
    
