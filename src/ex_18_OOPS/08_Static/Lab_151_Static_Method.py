class Utility:

    @staticmethod
    def greet(name):
        print("Hi",name)

    def greet_coursename(self,name):
        print("Hello",name)


Utility.greet("Pramod")

obj_ref= Utility()
obj_ref.greet_coursename("Prajwal")