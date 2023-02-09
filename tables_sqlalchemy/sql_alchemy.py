from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, create_engine, Date
from sqlalchemy.ext.declarative import declarative_base
import os.path

file_path = os.path.abspath(os.path.dirname(__file__))
engine = create_engine(f'sqlite:///{os.path.join(file_path, "project.db")}')
Base = declarative_base()


class Project(Base):
    __tablename__ = 'Project'
    id = Column(Integer, primary_key=True)
    first_name = Column("First_name", String)
    last_name = Column("Last Name", String)
    date_of_birth = Column("Date of birth", Date)
    position = Column("Position", String)
    salary = Column("Salary", Float, default=1000)
    enrollment = Column("Enrollment date", Date, default=datetime.today)
    end_date = Column("End Date", Date, default=None)

    def __init__(self, first_name, last_name, date_of_birth, position, salary, end_date=None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.position = position
        self.salary = salary
        self.end_date = end_date

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} - {self.position} {self.enrollment}"


Base.metadata.create_all(engine)
