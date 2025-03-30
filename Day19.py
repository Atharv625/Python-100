
# Break statement
# The break statement is used to exit a loop prematurely.
# When a break statement is encountered, the loop is terminated immediately,
# and the program control moves to the next statement following the loop.
print("Using break statement:")
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)  # Output: 0, 1, 2, 3, 4
print("Loop exited at i =", i)

# Continue statement
# The continue statement is used to skip the current iteration of a loop
# and move to the next iteration.
print("\nUsing continue statement:")
for i in range(10):
    if i == 5:
        continue  # Skip the current iteration when i is 5
    print(i)  # Output: 0, 1, 2, 3, 4, 6, 7, 8, 9
print("Loop completed")