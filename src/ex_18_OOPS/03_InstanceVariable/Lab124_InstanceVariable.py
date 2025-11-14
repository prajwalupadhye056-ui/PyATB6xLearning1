a=10 # variable everywhere in the program

class Person:
    b=11  # instance variable(within the class)

    def print_info(self):
        c = 20 # local variable
        print(c)
        print(self.b)
        print(a)

obj_ref= Person()
#print(b) # not allowed
#print(c) #not allowed