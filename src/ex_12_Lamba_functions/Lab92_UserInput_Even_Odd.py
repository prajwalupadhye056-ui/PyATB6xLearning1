#Write a program to calculate even and odd
#def find_even_odd(num)
# if num % 2 == 0:
# print("Even")
# else:
#   print("odd")

user_input= int(input("Enter the number"))

check_number= lambda num : "Even" if num % 2 == 0 else "Odd"

result=check_number(user_input)
print(result)
