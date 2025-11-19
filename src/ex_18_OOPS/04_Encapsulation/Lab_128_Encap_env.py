from dotenv import load_dotenv
import os
class VMOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        load_dotenv()
        if self.email == os.getenv("USERNAME") and self.password == os.getenv("PASSWORD"):
            print("Allowed to login")
        else:
            print("Login failed")

email = input("Enter the vmo login email\n")
password = input("Enter the vmo login password\n")

vmo_obj_ref = VMOLoginPage(email, password)
vmo_obj_ref.login_confirm()
