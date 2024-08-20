from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeeTable:
    db_connection_string = "postgresql+psycopg2://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
    __scripts = {
        "insert into": text(
            'insert into employee ("first_name", "last_name", "email", "company_id", "phone") values (:new_name, :new_last_name, :new_email, :id_company, :phone_number)'),
        "update": text(
            'update employee set first_name=:first_name_new, last_name=:last_name_new, email =:new_email, company_id =:company_id_new, phone =:phone_new where id =:id_to_change')
    }
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_employees(self):
        return self.db.execute("select * from employee where company_id = 2703").fetchall()

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
        sql = text("select * from employee where id =:id_create")
        return self.db.execute(sql, id_create = id)
   
    def get_max_id(self):
        return self.db.execute("select MAX(id) from employee").fetchall()[0][0]
    
    def update(self, first_name, last_name, email, company_id, phone, id):
        return self.db.execute(self.__scripts["update"],
                               first_name_new = first_name, 
                               last_name_new = last_name,
                               new_email = email,
                               company_id_new = company_id, 
                               phone_new = phone,
                               id_to_change = id)

    def delete(self, id):
        sql = text("delete from employee where id = :id_to_delete")
        self.db.execute(sql, id_to_delete = id)