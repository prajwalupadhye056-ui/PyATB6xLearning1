class Person:
    # Attributes
    name = "Pramod"
    age = 52
    color = "green"

    # Behaviour
    def talk(self):
        print("I can talk")

    def sleep(self, name):  # Args with no return type
        print("I am method")
        print("Sleep", name)

    def sleep2(self, name):  # Args with return
        print("I am a method")
        return None

    def walk(self):
        print("I am walking")

# Objects
geeta = Person()
navin = Person()
amit = Person()

print(geeta.name)
geeta.sleep("Pramod")
