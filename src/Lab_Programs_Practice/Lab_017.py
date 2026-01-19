# Write a python program to define a function that takes num and len as arguments and
# return a string as 00 in the output

#I/P :1125 len :4
#O/P : 0025

#It is “output a fixed-length zero-padded string based only on the LENGTH,
# ignoring the number value.”

'''This function extracts the last digit using modulo operator and converts it to a string.
Then zfill pads leading zeros to match the required length.'''

def get_last_digits(num, length):
    return str(num % 10).zfill(length)

num = int(input("Enter the number: "))
length = int(input("Enter the length: "))

print(get_last_digits(num, length))