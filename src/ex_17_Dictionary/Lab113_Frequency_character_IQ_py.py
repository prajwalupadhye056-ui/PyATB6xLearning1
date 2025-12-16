
#Frequeny of the character in a string
#Write a program to count the frequency
#of each character in the given string


string =input("\n Enter the input \n")

#Logic building
#input - "automation"
#dict ={"a" :2 ,"u" : 1, "t" : 2,"o": 2, "m":1 ,"i" :1 ,"n" : 1} - o/p

char_count ={}
for char in string:
    char_count[char] =char_count.get(char, 0) + 1
print(char_count)
