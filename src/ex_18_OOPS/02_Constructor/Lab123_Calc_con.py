class Calc:
    a = None
    b = None

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

obj_ref=Calc(10,6)
print(obj_ref.sum())
print(obj_ref.sub())
print(obj_ref.mul())
print(obj_ref.div())