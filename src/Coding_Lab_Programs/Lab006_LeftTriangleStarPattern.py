num = int(input("Enter the number of rows\n"))

for i in range(num, 0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()