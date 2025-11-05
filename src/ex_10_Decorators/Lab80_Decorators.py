# Decorators

def add_security(func):
    def wrapper():
        print("1.Before the function is called ")
        print("2.Add Helmet, Dashcash ,gloves ,knee guards")
        func()
        print("After the function is called")
        print("Secure driving ,Leave all the items")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("I am driving ola scooter")

@add_security
def drive_zypp_scooter():
    print("I am driving zypp scooter")
