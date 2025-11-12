string= "hello,world"
#vowel -a ,i,e,o,u

vowels ="aeiou"
vowels_count=0
result= list()

for char in string:
    if char in vowels:
        vowels_count= vowels_count+1
        result.append(char)

print(vowels_count)
print(result)


