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
    print("Palindrome")
   else:
     print("Not Palindrome")

else:
    print("Please Enter letters only")