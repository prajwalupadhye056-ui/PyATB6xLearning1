class Person:
    def say_name(self,name):
        print("Hi", name)

    def say_name(self, name ,lastname="Sheety"):
        print("Hi",name ,lastname)

obj_ref= Person()
obj_ref.say_name("Amit","upadhye")