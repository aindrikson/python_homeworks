from Employee import Employee
from EmployeeTable import EmployeeTable



api = Employee('https://x-clients-be.onrender.com')
db = EmployeeTable("postgresql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

def test_get_token():
    token = api.get_token
    assert token is not None


def test_get_list():
    api_res = api.get_list()
    assert len(api_res) > 0
    
    db_res = db.get_employees()
    assert len(api_res) == len(db_res)
    

def test_employee_add():
    
    res = api.add_new()
    employee_id = res["id"]
    
    db.delete(employee_id)
    
    
def test_get__change_info():
    db.add_new("Александра", "Индриксон", "testai@test.ru", "1418", "780800")
    max_id = db.get_max_id()
    
    new_employee = db.get_info(max_id)
    id_new_employee = new_employee[0]["id"]
    
    assert new_employee["id"] == max_id
    assert new_employee[-1][4] == "Александра"
    
    db.update("Мортикова", id_new_employee)
    
    
    db.delete(id_new_employee)



   

