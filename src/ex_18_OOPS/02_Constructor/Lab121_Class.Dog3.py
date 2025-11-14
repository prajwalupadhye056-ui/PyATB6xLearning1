class Dog:
    name =None
    breed= None
    height = None
    weight = None
    race = None

    def __init__(self,name,breed):
        print("Parametrized constructor")
        self.name=name
        self.breed=breed


    def bark(self):
        print("barking")

    def sleep(self):
        print("Who is sleep ->" + self.name)

    def talk(self):
           pass

chow =Dog("chow","mastiif")
rancho =Dog("rancho", "desi")

chow.sleep()
print(chow.name)
rancho.sleep()
print(rancho.name)
print(rancho.breed)