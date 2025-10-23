from ex_practice_programs.Lab10_Constructor import Calc


class ChildImpl(Calc):
    num2 = 200

    def __init__(self):
      Calc.__init__(self, 10, 15)

    def getcompleteData(self):
           return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getcompleteData())
