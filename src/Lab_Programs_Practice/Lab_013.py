#Write the python program to find duplicate characters in below list

#
words = ['india', 'is', 'my', 'country']
text = ' '.join(words)
print(text)

dup = []
for char in text:
    if text.count(char) > 1 and char not in dup:
        dup.append(char)

print(dup)
print(*dup)