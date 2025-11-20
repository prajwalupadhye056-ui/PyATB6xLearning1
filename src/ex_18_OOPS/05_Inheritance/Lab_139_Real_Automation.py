class BaseTest:
    def __init__(self,browser):
        self.browser= browser

    def setup(self):
        print(f"Launching {self.browser}")

class LoginTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running login test")

class SignupTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running signup Test")

t= LoginTest("Chrome")
t.run_test()

t= LoginTest("firefox")
t.run_test()