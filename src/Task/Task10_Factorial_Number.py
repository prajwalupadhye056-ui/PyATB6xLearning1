""" Question 1. :Given a Number a number you need to calculate the factorial of that number

# n = 5

# Fact = 5×4×3*2*1 = 120

# Fact = 0 → 1,
"""

num = int(input("Enter the number \n"))
fact =1

if num < 0:
    print(f"The number {num} is negative. Factorial does not exist for negative numbers.")
elif num == 0:
    print(f"The number {num} is zero. The factorial of 0 is always 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print(f"The factorial of {num} is {fact}")
