


from abc import ABC, abstractmethod

class Parent(ABC):

    def car(self):
        print("car")

    @abstractmethod
    def vcar(self):
        pass


class Child(Parent):
    def vcar(self):
        print("Vcar is present")


c = Child()
c.vcar()












