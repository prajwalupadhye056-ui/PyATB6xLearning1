#Write a program to print unique characters in string

text='test'
unique=[]

for char in text:
    if text.count(char) == 1 and char not in unique:
        unique.append(char)

print(unique)