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




print(Employee.num_of_empl)

emp_1 = Employee('Cory', "Kuku", 5000)
emp_2 = Employee('Test', 'User', 9000)
emp_3 = Employee('Alex', 'Bond', 9999)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


print(emp_1.__dict__)
print(Employee.__dict__)

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.20

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)

print(Employee.num_of_empl)

Employee.set_raise_amt(1.19)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)


emp_4_str = 'NIke-Helow-3000'
emp_5_str = 'Adidas-Kook-4000'
emp_6_str = 'Puma-Loom-5000'

first, last, pay = emp_4_str.split('-')
print(first, last, pay)
new_emp_4 = Employee(first, last, pay)
print(new_emp_4.pay)

new_emp_5 = Employee.from_string(emp_5_str)
print(new_emp_5.last)