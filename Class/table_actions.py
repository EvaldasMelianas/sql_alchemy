from tables_sqlalchemy.sql_alchemy import Project, Base, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime


class ProjectCRUD:

    def __init__(self):
        self.engine = engine
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_employee(self, first_name, last_name, date_of_birth, position, salary=1000):
        employee = Project(first_name, last_name, date_of_birth, position, salary)
        self.session.add(employee)
        self.session.commit()

    def change_salary(self, first_name, last_name, new_salary):
        employee = self.session.query(Project).\
            filter(Project.first_name == first_name, Project.last_name == last_name).first()
        employee.salary = new_salary
        self.session.commit()

    def delete_employee(self, employee_id):
        employee = self.session.query(Project).get(employee_id)
        self.session.delete(employee)
        self.session.commit()

    def fire_employee(self, employee_id):
        employee = self.session.query(Project).get(employee_id)
        employee.end_date = datetime.today()
        self.session.commit()

    def find_active(self, active=True):
        if active:
            employee = self.session.query(Project.first_name, Project.last_name, Project.position)\
                .filter(Project.end_date != "").all()
        else:
            employee = self.session.query(Project.first_name, Project.last_name, Project.position)\
                .filter(Project.active == "").all()
        return employee
