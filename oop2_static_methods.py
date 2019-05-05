from datetime import datetime
from datetime import date

'''
Instance methods automatically pass self
Class methods automatically aps cls
Static methods don't pass anything automatically and behaves like
regular functions except we include them in class, they have some logical
connection with a class

'''
class Employee:

    num_of_empl= 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + 'last' + '@company.com'
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

    '''Should use static method if we don't access class or instance variable
         in the method. People do mistakes and use instance/class methods when they need
         to use static instead.
    '''
import datetime
my_date = datetime.date(2016,7,10) # Sunday therefore False
my_date = datetime.date(2016,7,11)

print(Employee.is_workday(my_date))



