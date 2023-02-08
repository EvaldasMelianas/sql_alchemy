from Class.table_actions import ProjectCRUD

crud = ProjectCRUD()
"""crud.add_employee('Aurimas', 'Sprogimas', '1965-01-15', 'Team Lead', 3000)
crud.add_employee('Albertas', 'Suvis', '1990-10-15', 'Developer')
crud.add_employee('John', 'Goodman', '1973-02-30', 'Team quality manager', 2500)
crud.add_employee('Nic', 'Badman', '2000-05-10', 'Developer')
crud.add_employee('Jone', 'Eisena', '1999-06-17', 'Developer')
crud.add_employee('John', 'Walker', '1989-01-10', 'Product specialist', 2500)
crud.add_employee('Elena', 'Sulcaite', '2001-01-11', 'Developer')
crud.add_employee('Egle', 'Bartkeviciute', '2000-02-22', 'Developer')"""

crud.change_salary('Egle', 'Bartkeviciute', 3500)
#crud.fire_employee(7)
#print(crud.find_active())