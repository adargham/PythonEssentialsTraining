#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/



class Employee:

    num_of_emps = 0                # class variables should be the same for all instances
    raise_amt =  1.04

    def __init__(self, first, last, pay):          #__ are sometimes called dunder. We use special methods to create a more userfriendly print
        self.first = first                        # each is an instance variable whereas
        self.last  = last
        self.pay = pay
        self.email = first.lower() + '@'+ last.lower() +'.ch'

        Employee.num_of_emps += 1         # here we did not use the self because this is a constant that must not change between an employee and another

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)   # we can use Emplyee.raise_amount instead but this gives the flexilibity to change a signle instance

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{}, {}".format(self.fullname(), self.email)

emp_1 = Employee('Alain','Dargham',60000)
emp_2 = Employee('Mark', 'Dargham', 70000)

print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print(1+2)
print(int.__add__(1,2))
print('a'+'b')
print(str.__add__('a','b'))


