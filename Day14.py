# if else statement
# if else statement is used to check the condition and execute the code accordingly.
age=int(input("Enter your age: "))

print("You are",age,"years old.")
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# elif statement
# elif statement is used to check multiple conditions.
# If the first condition is false then it will check the next condition.
# If all the conditions are false then the else block will be executed.
if age>=18:
    print("You are eligible to vote.")
elif age==17:
    print("You will be eligible to vote next year.")
else:
    print("You are not eligible to vote.")
# Nested if else statement      
# Nested if else statement is used to check multiple conditions inside another if else statement.
# If the first condition is true then it will check the next condition.
# If all the conditions are false then the else block will be executed.
if age>=18:
    if age==18:
        print("You are eligible to vote for the first time.")
    else:
        print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# Short hand if else statement
# Short hand if else statement is used to write the code in a single line.  
print("You are eligible to vote.") if age>=18 else print("You are not eligible to vote.")



