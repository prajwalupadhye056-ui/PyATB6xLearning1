# Find the positive number is even or odd

num = int(input("Enter the number\n").strip())

if num >= 0:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Entered number is negative")

    # You can write short one liner condtions using ternary operator

    if num >= 0:
        print("Even" if num % 2 == 0 else "Odd")

    else:
        print("Negative number")
