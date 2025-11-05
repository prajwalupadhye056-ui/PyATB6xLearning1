num = int(input("Enter the number of rows to be printed: "))

for i in range(1, num + 1):
    # print spaces first
    print(" " * (num - i), end="")
    # then print stars
    print("*" * i)

    #print(" " * (num - i), end="") → prints spaces

#" " * (num - i) means: print some blank spaces before the stars.
#When i = 1: spaces = 5 - 1 = 4
#When i = 2: spaces = 3
#When i = 3: spaces = 2
#When i = 4: spaces = 1
#When i = 5: spaces = 0
#👉 This makes the stars shift left each line.

#print("*" * i) → prints stars

#"*" * i means: print i stars.

#When i = 1: *

#When i = 2: **

#When i = 3: *** and so on.