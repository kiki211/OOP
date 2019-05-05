"""
Methods which are surrounded by two underscores __
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

    def __repr__(self): # used for devs
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self): # used for end user
        return '{} - {}'.format(self.fullname(), self.email)


print(Employee.num_of_empl)

emp_1 = Employee('Cory', "Kuku", 5000)
emp_2 = Employee('Test', 'User', 9000)
emp_3 = Employee('Alex', 'Bond', 9999)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(repr(emp_1))
print(str(emp_1))
