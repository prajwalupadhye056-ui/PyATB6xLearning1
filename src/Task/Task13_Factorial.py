# Multiplication of natural numbers or it is the product of all positive integers less than or equal to n.

num = int(input("Enter the number \n"))

fact = 1
if num < 0:
    print("Fact! is not defined")

elif num == 0:
    print("Fact = ", fact)
else:
    for i in range(1, num + 1): #1,2,3,4,5
        fact = fact * i
    print(f"Factorial of the number is {fact}")
