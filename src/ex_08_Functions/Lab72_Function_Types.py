# User Defined

# 1. They can't return ->non return
# 2. They can return something
# 3. They have parameters
# 4. They don't have parameters/ arguments

import math

# built-in function

result = max(3, 4)
print(result)


# 1 .They can't return ->non return
# 2 No Return Type and No Parameter

def greet():
    print("Hello")


greet()


# 2 . No Return type and with Argument/Param

def greet_by_name(name):
    print("Hello", name)


greet_by_name("Prajwal")


# 3 .No return Type and with Default Argument

def say_hello_default_arg(name="Prajwal"):
    print("Hello", name.upper())


say_hello_default_arg("Dutta")
say_hello_default_arg()


# Multiple arguments

def multiple_args(name1="A", name2="B"):
    print("Mul -> ", name1, name2)


multiple_args()
multiple_args("Prajwal", "Upadhye")
multiple_args(name1="Prajwal")
multiple_args(name1="Upadhye", name2="Amit")
multiple_args(name2="Amit")


# def test(name)
#    return name
# test("test")


# 4. Argument + return type

def sum_of_two(a, b):
    return a + b


result = sum_of_two(4, 56)
print(result)


def sum_of_two_number_with_default(num1=100, num2=200):
    print("I will sum the two numbers")
    return num1 + num2


result = sum_of_two_number_with_default(num1=70, num2=80)
print(result)

result= sum_of_two_number_with_default()
print(result)
