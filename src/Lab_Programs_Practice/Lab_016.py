class A:
    def demo(self):
        print("In class A")

class B(A):
    def demo(self):
        print("In class B")

class C(A):
    def demo(self):
        print("In class c")


class D(B,C):    #Method resolution order[MRO]
    pass

test=D()
test.demo()

#o/P : In class B