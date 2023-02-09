from tables_sqlalchemy.sql_alchemy import Project, Base, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime


class ProjectCRUD:

    def __init__(self):
        self.engine = engine
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_employee(self, data):
        for name, surname, dob_str, position, *salary in data:
            salary = salary[0] if salary else 1000
            dob = datetime.strptime(dob_str, '%Y-%m-%d')
            employee = Project(name, surname, dob, position, salary)
            self.session.add(employee)
        self.session.commit()

    def change_salary(self, employee_id, new_salary):
        employee = self.session.query(Project).get(employee_id)
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
                .filter(Project.end_date.is_(None)).all()
        else:
            employee = self.session.query(Project.first_name, Project.last_name, Project.position)\
                .filter(Project.end_date.is_not(None)).all()
        return employee

    def find_pay_above(self, value: int):
        query = self.session.query(Project).filter(Project.salary > value).get(Project.position, Project.salary)
        return query

    def find_by_fragment(self, value):
        frg_name = self.session.query(Project).filter(Project.first_name.contains(value)).all()
        frg_surname = self.session.query(Project).filter(Project.last_name.contains(value)).all()
        while True:
            return frg_name or frg_surname
