# Exception handling
a=input("Enter the amount:")
print(f"Multiplication table of {a} is :")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i}={int(a)*i}")
except Exception as e:
    print("INvalid input")
finally:
    print("exception handling")



x=int(input("enter the first number"))
y=int(input("enter the second element"))

try:
    result=x/y
except ZeroDivisionError as e:
    print("you try to divide by zero")
finally:
    print("Division succefully")

