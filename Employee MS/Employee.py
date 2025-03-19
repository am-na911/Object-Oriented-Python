class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee {self.name} has {self.age} age and salary {self.salary}'

    # def __repr__(self):
    #     return f'Employee(name={self.name}, age={self.age}, salary={self.salary})'

emp = Employee('amna', 21, 25000)
print(emp)

    