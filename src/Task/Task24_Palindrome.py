#Question - ✅Palidrome of String

"""🧩 Example Walkthrough
Let’s take the word "level":

Forward: "level"
Backward: "level"
Both are identical → Palindrome ✅
Now, "hello":
Forward: "hello"
Backward: "olleh"
"""

string = input("Enter a string: ")

if string.isalpha():  # checks if input has only letters
   if string == string[::-1]:
    print(f"Entered string {string} is a Palindrome")
   else:
     print(f"Entered string {string} is Not a Palindrome")

else:
    print("Please Enter letters only")