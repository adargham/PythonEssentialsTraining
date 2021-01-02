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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp_1 = Employee('Alain','Dargham',60000)
emp_2 = Employee('Mark', 'Dargham', 70000)

import datetime

my_date = datetime.date(2021, 1, 4)
print(my_date)
print(Employee.is_workday(my_date))