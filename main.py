from Class.table_actions import ProjectCRUD

crud = ProjectCRUD()
crud.add_employee([('Aurimas', 'Sprogimas', '1965-01-15', 'Team Lead', 3000),
                   ('Albertas', 'Suvis', '1990-10-15', 'Developer'),
                   ('John', 'Goodman', '1973-02-28', 'Team quality manager', 2500),
                   ('Nic', 'Badman', '2000-05-10', 'Developer'),
                   ('Jonas', 'Vabinskas', '1989-01-10', 'Product specialist', 2500),
                   ('Albertas', 'Jonauskas', '1989-01-10', 'Product specialist', 2500),
                   ('Sarunas', 'Aurimas', '1989-01-10', 'Product specialist', 2500),
                   ('Egle', 'Bartkeviciute', '1989-01-10', 'Product specialist', 2500),
                   ('Elegija', 'Barstkeviciute', '1989-01-10', 'Product specialist', 2500)])

crud.change_salary(8, 3500)
crud.fire_employee(7)
print(crud.find_active(False))
print(crud.find_pay_above(1500))
print(crud.find_by_fragment('Aur'))