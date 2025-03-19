from EmployeesManager import *

class FrontendManager:
    def __init__(self):
        self.EmployeesManager = EmployeeManager()

    def print_menu(self):
        print('\nprogram options: ')
        messages = [
            '1) Add a new employee',
            '2) List all employee',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
               ]
        print('\n'.join(messages))
        user_input = f'Enter your choice (from 1 to {len(messages)}): '
        return input_is_valid(user_input, 1, len(messages))
    
    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.EmployeesManager.add_employee()
            elif choice == 2:
                self.EmployeesManager.list_employee()
            elif choice == 3:
                age_from = int(input('Enter age from: \n'))
                age_to = int(input('Enter age to:'))
                self.EmployeesManager.del_employe_with_age(age_from,age_to)
            elif choice == 4:
                name = str(input('Enter the name: '))
                salary = int(input('Enter the salary: '))
                self.EmployeesManager.update_salary_by_name(name, salary)
            else:
                break

