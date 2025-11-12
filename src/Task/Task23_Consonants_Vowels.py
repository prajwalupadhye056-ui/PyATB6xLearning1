#Question - ✅ Count vowels and consonants in a String


string ="Prajwal"

vowels ="aeiou"

vowels_count=0
consonants_count = 0

vowel_list = []        # to store vowels
consonant_list = []    # to store consonants

for char in string:
    if char in vowels:
        vowels_count= vowels_count+1
        vowel_list.append(char)
    else:
        consonants_count= consonants_count+1
        consonant_list.append(char)

print(vowels_count)
print(consonants_count)
print(vowel_list)
print(consonant_list)

