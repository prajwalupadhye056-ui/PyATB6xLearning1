str = input("Enter the string \n").strip()

if str.isdigit():
    print("Enter the valid string")

elif str == str[::-1]:
    print(f"The string {str} is palindrome")
else:
    print( f" The string {str} is not a palindrome")
