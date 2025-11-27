class InvalidAgeException(Exception):
    pass

def check_div_zero(a):
    if a == 0:
        raise ZeroDivisionError("Can't divide with zero")

def can_you_drink(age):
    if age < 18:
        raise InvalidAgeException("Invalid age of drinking")


#can_you_drink(12)
can_you_drink(32)
