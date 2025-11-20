class APIBase:

    def api_auth(self):
        print("Authentication API")

class DBBase:
    def db_connect(self):
        print("Connecting to the DB")

class HybridTest(APIBase,DBBase):
    def run(self):
        self.api_auth()
        self.db_connect()
        print("Test case Running")

tc1 = HybridTest()
tc1.run()
