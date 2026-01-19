#Write a python program to count the instances of a class in python

class A:
    count=0
    def __init__(self):
        A.count=A.count+1
        print("Class A is called")

a1=A()
print(A.count)