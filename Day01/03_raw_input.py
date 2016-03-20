#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'niming'

name = raw_input("Please input your name:")
age = input("age:")
job = raw_input("job:")
salary = raw_input("salary:")


print type(age)
print type(age)

print '''
Personal information of %s:
    Name: %s
     Age: %d
     Job: %s
  Salary: %s
''' % (name, name,age,job,salary)