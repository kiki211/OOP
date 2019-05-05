import datetime
"""
Method resolution order - when we create a subclass and it doesn't have constructor
it goes and take it from Parent(Super) class
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
"""
class Employee:

    num_of_empl= 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_empl += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod #decorator
    def is_workday(day): # we just pass the arguments we want to work with
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

"""We only inherit class variables and instance methods
"""
class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # to keep it DRY and more maintainable
        # we take all existing arguments from parent class
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


#print(help(Developer))
dev1 = Developer('Jack', 'Hoop', 120000, 'Python')
dev2 = Developer('Jone', 'Doop', 90000, 'Java')

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

print(dev1.email)
print(dev1.prog_lang)

mgr1 = Manager('Sue', 'Smith', 90000, [dev1])
print(mgr1.email)
mgr1.print_emp()
print ('____________________________')
mgr1.add_emp(dev2)
mgr1.print_emp()
mgr1.remove_emp(dev2)
mgr1.print_emp()


'''
Quick tricks
'''

print(isinstance(dev2, Developer))
print(isinstance(dev2, Employee))
print(isinstance(dev2, Manager))


print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))