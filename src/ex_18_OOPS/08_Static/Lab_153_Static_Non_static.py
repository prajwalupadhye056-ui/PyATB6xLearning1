class MathOperation:

    def div(self,a,b):
           return a / b

    @staticmethod
    def sum(a,b):
        return a+b

t=MathOperation()
print(t.div(9,6))
print(MathOperation.sum(5,9))
