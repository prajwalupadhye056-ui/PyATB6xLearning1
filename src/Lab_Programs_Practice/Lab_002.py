# Implement inheritance and Super keyword in python


'''class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def helloGreet(self):
        return "Hello from child"

obj=Child()
obj.helloGreet()
obj.greet() '''

#Super() -It is the Keyword use to call Parent methods within the class

class Parent:
    def greet(self):
        return "Hello from Parent"

    print("From the Parent method")

class Child(Parent):
    def greet(self):
        return super().greet() +"Hello from Child"


obj=Child()
obj.greet()