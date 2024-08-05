from Employee import Employee
import pytest
import requests

api = Employee('https://x-clients-be.onrender.com')

def test_get_token():
    token = api.get_token
    
    assert token is not None


def test_get_list():
    res = api.get_list()
    
    assert len(res) > 0


def test_employee():
    res = api.add_new()
    employee_id = res["id"]
    
    new_employee = api.get_info(employee_id)
    
    assert new_employee["id"] == employee_id

    change_employee = api.change_info(employee_id)
    new_email = change_employee["email"]
    
    assert change_employee["id"] == employee_id
    assert change_employee["email"] == new_email
    assert change_employee["isActive"] == True


   

