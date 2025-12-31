#Encapsulation
# Hide the data members (class variables , instance variables)
#by using only the methods

class Car:

    def __init__(self):
        self.password= "pramod"
        self.__password="pass123" #private

    def nany(self):
      self.__password="6934"
      print(self.__password)


object_ref= Car()

print(object_ref.password)
#print(object_ref.__password)- # not allowed
object_ref.nany()

