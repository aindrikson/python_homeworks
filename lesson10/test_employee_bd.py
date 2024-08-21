from Employee import Employee
from EmployeeTable import EmployeeTable
import allure


api = Employee('https://x-clients-be.onrender.com')
db = EmployeeTable("postgresql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

@allure.epic("Employee BD")
@allure.severity(severity_level='normal')
@allure.title("Получение токена авторизации")
@allure.description("Получение токена авторизации и его проверка")
@allure.feature('GETTOKEN')
def test_get_token():
    with allure.step("Получение токена авторизации через API"):
        token = api.get_token
    with allure.step("Проверка токена авторизации"):
        assert token is not None

@allure.epic("Employee BD")
@allure.severity(severity_level='normal')
@allure.title("Список сотрудников компании")
@allure.description("Получение списка сотрудников компании из БД и АПИ. Сравнение списков.")
@allure.feature('GETLIST')
def test_get_list():
    with allure.step("Получение списка сотрудников компании из АПИ"):
     api_res = api.get_list()
    with allure.step("Проверка списка"):
     assert len(api_res) > 0
    with allure.step("Получение списка сотрудников компании из БД"):
     db_res = db.get_employees()
    with allure.step("Сравнение списков сотрудников, полученных из АПИ и БД"):
     assert len(api_res) == len(db_res)
    
@allure.epic("Employee BD")
@allure.severity(severity_level='normal')
@allure.title("Добавление сотрудника через АПИ и последующее удаление из БД")
@allure.description("Добавление нового сотрудника через АПИ и его последующее удаление из БД")
@allure.feature('ADD EMPLOYEE')
def test_employee_add():
    with allure.step("Добавление нового сотрудника через АПИ"):
        res = api.add_new()
    with allure.step("Получение id добавленного сотрудника"):
        employee_id = res["id"]
    with allure.step("Удаление сотрудника из БД"):
        db.delete(employee_id)
    
@allure.epic("Employee BD")
@allure.severity(severity_level='normal')
@allure.title("Добавление и редактирование сотрудника")
@allure.description("Добавление нового сотрудника через БД, изменения сотрудника и его удаление")
@allure.feature('ADD AND CHANGE EMPLOYEE')
def test_get_change_info():
    with allure.step("Добавление нового сотрудника в БД"):
        db.add_new("Александра", "Индриксон", "testai@test.ru", "3374", "780800")
    with allure.step("Получение id нового сотрудника через БД"):
        max_id = db.get_max_id()
    with allure.step("Получение информации о сотруднике через АПИ"):
        new_employee = api.get_info(max_id)
    with allure.step("Проверка, что id из БД и АПИ соответсвуют друг другу"):
        assert new_employee["id"] == max_id
    with allure.step("Обновление информации о добавленном сотруднике"):
        db.update("Aleksandra", "Indrikson", "aindrikson@test.bd", "3374", "210021", max_id)
    with allure.step("Проверка, что id сотрудника не изменилось"):
        change_employee = api.get_info(max_id)
    with allure.step("Значение поле email сохранить в переменную"):
        new_email = change_employee["email"]
    with allure.step("Изменение успешно внесены"):
        assert change_employee["id"]== max_id
        assert change_employee["email"]== new_email
    with allure.step("Удаление сотрудника"):
        db.delete(max_id)



   

