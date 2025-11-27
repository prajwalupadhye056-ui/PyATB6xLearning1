class Home:

    def __init__(self):
        self.public_var="father"
        self._protected_var= "brother"
        self.__private_var= "baby"


    def mom(self):
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("Private wife")

object_ref= Home()
object_ref.__wife() # not allowed
object_ref.__private_var # not allowed

object_ref.mom()
print(object_ref._protected_var) #but not recommneded

