# Find the first non-repeating character in a string using set
# swiss - >s -x w-answer

"""print("swiss".count("s"))
print("swiss".count("w"))
print("swiss".count("i"))
"""


s= set()

def non_repeating_char(string):
      for char in string:
          if string.count(char)==1:
              s.add(char)
              return char
          return None

print(non_repeating_char("Swiss"))

print(s)