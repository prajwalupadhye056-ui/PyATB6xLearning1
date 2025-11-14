class Calc:
    a = None
    b = None

    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return a + b


    def sub(self, a ,b):
        return a - b

    def mul(self,a ,b):
        return a * b

    def div(self,a ,b):
        return a / b

a= float(input("\n Enter the value of a\n"))
b= float(input("\n Enter the value of b\n"))

obj_ref= Calc()

output_sum = obj_ref.sum(23,10)
output_sub = obj_ref.sub(30,20)
output_mul = obj_ref.mul(20,3)
output_div = obj_ref.div(21,10)

print(output_sum,output_sub,output_mul,output_div)