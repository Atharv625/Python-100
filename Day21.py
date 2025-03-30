def sum(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):

    return a * b
def divide(a,b):

    return a / b
def power(a,b):
    return a ** b
def modulo(a,b):
    return a % b
def floor_division(a,b):
    return a // b
def absolute(a):

    if a < 0:
        return -a
    return a
def square_root(a):
    return a ** 0.5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def gcd(a, b):
    while b:
        a, b = b, a % b

    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
def prime_factors(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors
print(sum(5, 3))  # 8
print(subtract(5, 3))  # 2
multiply(5, 3)  # 15
divide(5, 3)  # 1.6666666666666667
power(5, 3)  # 125
modulo(5, 3)  # 2
floor_division(5, 3)  # 1
absolute(-5)  # 5
square_root(25)  # 5.0
factorial(5)  # 120
fibonacci(5)  # 5
gcd(12, 15)  # 3
lcm(12, 15)  # 60
prime_factors(28)  # [2, 2, 7]
# Compare this snippet from Python-100.2/Day19.py:
#
