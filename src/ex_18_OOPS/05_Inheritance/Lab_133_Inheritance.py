# Single inheritance

class BaseTest:
    driver = "Chrome"
    __driver2= "Firefox"

    def setup(self):
        print("Base setup with browser and env")
        print("Base setup with browser and ->" + self.__driver2)

class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print("Running the test cases - >" + self.driver)
      #  print("Running the test cases - >" + self.__driver2) Not allowed

t = LoginTest()
t.run()
