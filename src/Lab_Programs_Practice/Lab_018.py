#Write a python program that takes
# n number of input from the user
#Print n number of triangles
#Print even number of lines if it is even
#Print odd number of lines if it is odd

#Requirement understood:

#Take n as input from the user

#Print n triangles

#If the triangle number is even, print "Even"

#If the triangle number is odd, print "Odd"

#Each triangle prints lines equal to its number

n = int(input("Enter number of triangles: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"\nTriangle {i} - Even")
    else:
        print(f"\nTriangle {i} - Odd")

    for j in range(1, i + 1):
        print(str(i) * j)

