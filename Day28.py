# fstring
# fstring is a way to format strings in Python
# fstring is a way to format strings in Python 3.6 and above
str="hey my name is {name} and I am {age} years old"

name="John"
age=25
print(f"{str}")
print(f"{str.format(name=name, age=age)}")
print(f"hey my name is {name} and I am {age} years old")
str2="hey my class is {class1} and I am {age} years old"
class1="python"
age=25
print(f"{str2.format(class1=class1, age=age)}")