class VMOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "prajwal.upadhye056@gmail.com" and self.password == "admin123":
            print("Allowed to login")
        else:
            print("Login falied")


email = input("Enter the vmo login email\n")
password = input("Enter the vmo login password\n")

vmo_obj_ref = VMOLoginPage(email, password)
vmo_obj_ref.login_confirm()
