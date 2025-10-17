# Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (eg. A,B,C, D or F)
# based on following grading scale
from selectors import SelectSelector

# A :90 -100
# B :80-89
# C :70-79
# D: 60-69
# F: 0-59

# Logic building formula

# I/P : User Input -Int
# O/P : ->str ->A ,B

score = int(input("Enter the score :\n").strip())

if score > 100 or score <= -1:
    print("You  are Superman!!,you can't get grade")

else:
    if score >= 90 and score <= 100:
        print("Your grade is A")
    elif score >= 80 and score <= 89:
        print("Your grade is B")
    elif score >= 70 and score <= 79:
        print("Your grade is C")
    elif score >= 60 and score <= 69:
        print("Your grade is D")
    else:
         print("Your grade is F")

#float, #ABC ->Try catch