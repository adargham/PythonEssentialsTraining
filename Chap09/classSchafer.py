#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay = pay
        self.email = first.lower() + '@'+ last.lower() +'.ch'

    def fullname(self):
        return f'{self.first} {self.last}'



emp_1 = Employee('Alain','Dargham',60000)
emp_2 = Employee('Mark', 'Dargham', 70000)


print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

x = emp_1.fullname()
y = Employee.fullname(emp_1)

print(x)
print(y)

print(emp_2.fullname())