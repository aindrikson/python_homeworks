import requests
import allure
class Employee:

    def __init__(self, url):
        self.url = url 


    @allure.step("api. Получение токена авторизации")
    def get_token(self):
     log_pass = {
        'username' : 'raphael', 
        'password' : 'cool-but-crude'
     }
     resp = requests.post(self.url+'/auth/login', json=log_pass)
     token = resp.json()['userToken']
     return token
    
    @allure.step("api. Получение списка сотрудников компании")
    def get_list(self):
       company = {'company' : '3374'}
       response = requests.get(self.url+'/employee', params=company)
       return response.json()
    
    @allure.step("api. Добавление нового сотрудника в компанию")
    def add_new(self):
       token = self.get_token()
       headers = {'x-client-token' : token}
       body = {
       "id": 1704,
       "firstName": "Aleksandra",
       "lastName": "Indrikson",
       "middleName": "Igorevna",
       "companyId": 3374,
       "email": "ai@test.ru",
       "url": "ai.com",
       "phone": "780800",
       "birthdate": "2020-08-04T10:34:32.326Z", 
       "isActive": True
       }
       response = requests.post(self.url+'/employee/' , headers=headers, json=body)
       return response.json()
    
    @allure.step("api. Получение информации о сотруднике по {employee_id}")
    def get_info(self, employee_id):
       response = requests.get(self.url+'/employee/' + str(employee_id))
       return response.json()
    
    @allure.step("api. Изменение информации о сотруднике по {employee_id}")
    def change_info(self, employee_id):
       token = self.get_token()
       body = {
       "lastName": "Mortikova",
       "email": "aimortikova@test.ru",
       "url": "aimor.com",
       "phone": "780878",
       "isActive": True
       }
       headers = {'x-client-token' : token}
       response = requests.patch(self.url+'/employee/' + str(employee_id), headers=headers, json=body)
       return response.json()