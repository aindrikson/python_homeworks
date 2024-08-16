from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeeTable:
    db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
    __scripts = {
        "insert into": text(
            'insert into employee ("first_name", "last_name", "email", "company_id", "phone") values (:new name, :new_last_name, :new_email, :id_company, :phone_number)'
        )
    }
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_employees(self):
        return self.db.execute("select * from employee where company_id = 1418").fetchall()

    def add_new(self, first_name, last_name, email, company_id, phone):
        return self.db.execute(
            self.__scripts["insert into"],
            new_name = first_name,
            new_last_name = last_name,
            new_email = email,
            id_company = company_id,
            phone_number = phone
        )
    
    def get_info(self, id):
        sql = text("select * from employee where id = :id_create")
        self.db.execute(sql, id_create = id)
   
    def get_max_id(self):
        return self.db.execute("select MAX(id) from employee").fetchall()[0][0]
    
    def update(self, last_name, id):
        return self.db.execute("update employee set last_name = :last_name_new where id = :id_to_change", last_new_name = last_name, id_to_chage = id)
    
    
    def delete(self, id):
        sql = text("delete from employee where id = :id_to_delete")
        self.db.execute(sql, id_to_delete = id)