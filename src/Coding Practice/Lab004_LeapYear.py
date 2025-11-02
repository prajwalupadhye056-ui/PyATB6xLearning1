# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

# Leap Year Rules:

"""A year is a leap year if it's divisible by 4 AND not divisible by 100
OR if it's divisible by 400

// Leap year rule:
        // 1. Divisible by 4 → leap year
        // 2. Except years divisible by 100 → not leap year
        // 3. But if divisible by 400 → leap year again
"""

year =int(input("Enter the year \n"))

if year < 0:
     print("Enter valid year")

elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")


