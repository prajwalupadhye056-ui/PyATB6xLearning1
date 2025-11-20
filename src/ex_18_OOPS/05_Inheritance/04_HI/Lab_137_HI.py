from multiprocessing.util import LOGGER_NAME


class BaseTest:
    def setup(self):
        print("Setup the BaseTest")

class LoginTest(BaseTest):
    def run(self):
        print("Running Login Test")

class SignupTest(BaseTest):
    def run(self):
        print("Signing up test")

LoginTest().run()
LoginTest().setup()
SignupTest().run()
SignupTest().setup()