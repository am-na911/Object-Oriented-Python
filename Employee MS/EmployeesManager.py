from utility import *
from Employee import *

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('Enter employee data')
        name = str(input('Enter the name of the employee: '))
        age = int(input('Enter the age of the employee: '))
        salary = int(input('Enter the salary of the employee: '))
       
        emp = Employee(name, age, salary)
        self.employees.append(emp)

    def list_employee(self):
        if len(self.employees) == 0:
            print('The list is empty')
        else:
            for emp in self.employees:
                print(emp)

    def del_employe_with_age(self, age_from, age_to):
        for emp in self.employees[:]:
            if age_from <= emp.age <= age_to:
                print( f'\tDeleting Employee {emp.name}')
                self.employees.remove(emp)

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None
                    
    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)
        if emp is None:
            print('Error: No employee found')
        else:
            emp.salary = salary 
           