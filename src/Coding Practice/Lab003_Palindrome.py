str = input("Enter the String \n").strip()

if str.isdigit():
    print("Please enter valid string.")

elif str == str[::-1]:
    print(f"The string {str} is palindrome")
else:
    print(f"The string {str} is not palindrome")
