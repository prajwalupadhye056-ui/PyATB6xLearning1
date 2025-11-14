num =int(input("Enter the number of rows to be printed \n"))

for i in range(1,num +1):
    for j in range (i):
        print("*",end="")
    print()