from abc import ABC ,abstractmethod

class Father(ABC):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def loan(self):
        pass

class Amit(Father):
    def loan(self):
        print("Loan is with me")

obj_ref=Amit("Amit Shedge")
obj_ref.loan()
