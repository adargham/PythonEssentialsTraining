#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/



class Employee:

    num_of_emps = 0                # class variables should be the same for all instances
    raise_amt =  1.04

    def __init__(self, first, last, pay):
        self.first = first                        # each is an instance variable whereas
        self.last  = last
        self.pay = pay
        self.email = first.lower() + '@'+ last.lower() +'.ch'

        Employee.num_of_emps += 1         # here we did not use the self because this is a constant that must not change between an employee and another

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)   # we can use Emplyee.raise_amount instead but this gives the flexilibity to change a signle instance

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first, last, pay)

emp_1 = Employee('Alain','Dargham',60000)
emp_2 = Employee('Mark', 'Dargham', 70000)

Employee.raise_amt = 1.05 # another way to change the variable without the class method

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.set_raise_amt(1.08)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)



emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steven-Smith-30000'
emp_str_3 = 'Sofie-Hartmann-40000'

first,last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first,last,pay)

new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_2)

print(new_emp_2. email)

print(new_emp_1.email)
print(new_emp_1.pay)
