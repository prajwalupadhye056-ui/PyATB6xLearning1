# Program to count number of characters in given  string using dictionary

ntr = input("Enter the String\n").strip()

# creating empty dictionary
char_count = {}
for char in ntr:
    if char in char_count:
        char_count[char]=char_count[char]+1
    else:
        char_count[char]=1
        print(char_count)
