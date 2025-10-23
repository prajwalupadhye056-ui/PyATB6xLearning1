#Self keyowrd is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__

#default constructor
class Calc:
    num = 100 #class variables

    #default constructor

    def __init__(self,a,b):
        self.firstNumber=a #instance variables
        self.secondNumber=b
        print("I am the constructor i am called when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber+self.secondNumber+ Calc.num



obj=Calc(2,3) #syntax to create objects in python
obj.getData()
print(obj.Summation())

obj1=Calc(4,9) #syntax to create objects in python
obj1.getData()
print(obj1.Summation())