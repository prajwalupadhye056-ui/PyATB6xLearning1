class TestExample:

    def __init__(self):
        self.driver = "Chrome"
        self._config = "STAG"
        self.__api_key = "ABC12563"


    def show(self):
           print(f"Driver :{self.driver}")
           print(f"Config : {self._config}")
           print(f"Api Key: {self.__api_key}")

    def __private_method1(self):
        pass


    def __private_method2(self):
        pass

    def work(self):
        self.__private_method1()
        self.__private_method2()

obj = TestExample()
obj.show()
obj.work()

#Access Levels
print(obj.driver) # accessible
print(obj._config) # not recommended
#print(obj.__api_key) # this not allowed