class Testsuite:
    def info(self):
        print("Test suite information")


class BaseTest(Testsuite):
    def setup(self):
        print("Base setup")

    def run(self):
        print("Base Test Execution")

class LoginTest(BaseTest):
    def run(self): #overiding
        print("Login Test Execution")

class APITest(BaseTest):
    def run(self):
        print("API test execution")

t= LoginTest()
t.run()

