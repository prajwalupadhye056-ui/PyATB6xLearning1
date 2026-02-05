class BaseTest():
    def run(self):
        print("Running generic Test")

class LoginTest(BaseTest):
    def run(self):

        print("Running Login Test")

t= LoginTest()
t.run()