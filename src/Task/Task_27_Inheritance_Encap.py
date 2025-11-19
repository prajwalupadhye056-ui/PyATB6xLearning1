"""Build a Test Framework with Encapsulation + Inheritance

#🎯 Goal:

#Create a simple automation structure that uses:

A BaseTest class for setup/teardown (Parent class)

A LoginTest class that inherits BaseTest (Child class)

Encapsulate sensitive data (like credentials) as private variables


✅ Requirements:

Create a BaseTest class:

Has a protected variable _driver = "Chrome".

Method setup() prints "Launching browser: Chrome".

Method teardown() prints "Closing browser".

Create a LoginTest class that inherits BaseTest:

Has private variables for username and password.

Method run_test() that prints:

"Running login test with user: <username>".

Use encapsulation: access private vars only through a method (e.g., get_user()).

Create an object of LoginTest and call:

setup()

run_test()

teardown()"""

#Launching browser: Chrome

#Running login test with user: admin

#Closing browser

class BaseTest:
    _driver = "Chrome"

    def setup(self):
        print(f"Launching browser:{self._driver}")

    def teardown(self):
        print("Closing broswer")

class LoginTest(BaseTest):
    __username="admin"
    __password="89653"

    def get_user(self):
        return self.__username

    def run_test(self):
       user = self.get_user()
       print(f"Running login test with user:{user}")

obj_ref= LoginTest()
obj_ref.setup()
obj_ref.run_test()
obj_ref.teardown()
