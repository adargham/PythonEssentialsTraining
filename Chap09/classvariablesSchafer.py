#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/



class Employee:

    num_of_emps = 0                # class variables should be the same for all instances
    raise_amount =  1.04

    def __init__(self, first, last, pay):
        self.first = first                        # each is an instance variable whereas
        self.last  = last
        self.pay = pay
        self.email = first.lower() + '@'+ last.lower() +'.ch'

        Employee.num_of_emps += 1         # here we did not use the self because this is a constant that must not change between an employee and another

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   # we can use Emplyee.raise_amount instead but this gives the flexilibity to change a signle instance

print(Employee.num_of_emps)

emp_1 = Employee('Alain','Dargham',60000)
emp_2 = Employee('Mark', 'Dargham', 70000)

print(Employee.num_of_emps)

print(emp_1.__dict__)
emp_1.raise_amount = 1.06
print(emp_1.__dict__)

Employee.raise_amount = 1.05

print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)



