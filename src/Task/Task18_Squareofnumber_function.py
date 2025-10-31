"""
Q - Create a function which will take a positive number from the user and perform square
of the number?

i/o = 3

o/p = 9
"""
def square(num):

    if num > 0:
        print(num ** 2)
    else:
        print("Enter the number greater than 0")

square(int(input("Enter the positive number")))




