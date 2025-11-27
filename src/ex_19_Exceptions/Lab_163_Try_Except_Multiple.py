a = int(input("Enter num 1"))
b = int(input("Enter num 2"))

try:
    c = a / b
    print(c)
except (NameError, TypeError, IndexError, ZeroDivisionError):
     print("Error due to Name,Type, Index ,zero division error")
