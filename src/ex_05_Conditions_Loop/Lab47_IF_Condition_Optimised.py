# Write a program to take user age and
# let him know if he can go to club
# 21

# Step 1
# i/p : age,int
# o/p : String (result- Can go to club or not)

# Step 2 : Rough Logic(brute force)

"""
age >21 -> print can go
age < 21-> print can't go


"""
# Step 3 .Write the logic

age = int(input("Enter the age \n").strip())

if age <= 0 or age > 130:
    print("Please Enter valid age")

else:
    if age >= 21:
        print("Yes ,can go to the club")
    else:
        print("No, can't go the club")

# Step 4 . check the edge cases.

# we should consider edge cases such as :
# Negative ages or extremely high values -> program will break
# Non-numeric input -ABC
# Age which is valid >130

# Step 5. Optimise the code
# Handle all the edges
