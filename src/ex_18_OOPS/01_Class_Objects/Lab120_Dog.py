class Dog:
    name= None
    breed = None
    height =  None
    weight =None

    def bark(self):
        print("Barking")
        # print(name) -not allowed
        print(self.name)

    def talk(self):
        print("Talking")

print("Outside the class")

chow =Dog()
rancho =Dog()
