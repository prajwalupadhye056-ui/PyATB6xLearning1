#Write a python program to count of occurrences of 'i' in given string "chirinjibi"



text= "chirinjibi"
count=0

for char in text:
    if char =='i':
        count= count+1

print(f"Number of occurrences of 'i':{count}")

