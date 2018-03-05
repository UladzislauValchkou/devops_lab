#!/bin/python
#pylint:disable=invalid-name
""" task 2 """
word = str(input("Enter your word"))
x = word[::-1]
if word == x:
    print("current word is a polydrome")
else:
    print("current word is not a polydrome")
