# classes are user defined blueprint or prototype

# methods, class variables, instance variables and constructor
# objects for the classes

class Calc:
    num = 100

    def getData(self):
        print("I am now executing as method in class")


obj=Calc() #syntax to create objects in python
obj.getData()
print(obj.num)

