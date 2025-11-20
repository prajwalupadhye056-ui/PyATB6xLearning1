"""🎯 Goal:

Simulate a secure API testing structure where:
The BaseAPI class holds an encapsulated token (private).
The UserAPI class inherits from BaseAPI and uses that token to call a fake endpoint.

✅ Requirements:
Create a BaseAPI class:
Private variable __token = "ABC123SECRET".
Protected method gettoken() returns this token safely.
Create a UserAPI class that inherits BaseAPI:
Method get_user_data() prints:
"Fetching user data using token: <token>".
Create an object of UserAPI and call get_user_data()."""


class BaseAPI:
    __token = "ABC123SECRET"

    def _gettoken(self):
        return self.__token


class UserAPI(BaseAPI):

    def get_user_data(self):
        print(f"Fetching user data using token: {self._gettoken()}")

obj_ref= UserAPI()
obj_ref.get_user_data()
