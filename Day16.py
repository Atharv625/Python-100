import os
# match case statement in python
# match case statement is used to compare the value of a variable with multiple values
x=int(input("enter the number of x: "))
match x:
    case 0:
        print("x is 0")
    case 1:
        print("x is 1")
    case _: 
        print("x is other number")