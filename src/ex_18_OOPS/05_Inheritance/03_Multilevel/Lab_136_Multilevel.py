class TestSuite:
    def info(self):
        print("This is GF - Step 1")

class BaseTest(TestSuite):
    def setup(self):
        print("BaseTest -F -Step2")

class UITest(BaseTest):
    def run(self):
        self.info()
        self.setup()
        print("Running the test case")

tc3 = UITest()
tc3.run()

