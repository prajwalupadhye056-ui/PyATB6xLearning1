num = int(input("Enter the number\n"))
fact=1

if num < 0:
    print(f"The number {num} is negative.Factorial does not exist for negative numbers")
elif num == 0:
    print(f"The number {num} is 0 .The factorial of the 0 is always 1")
else:
    for i in range(1,num + 1):
        fact = fact *i
    print(f"The factorial of the given number {num} is", fact)
