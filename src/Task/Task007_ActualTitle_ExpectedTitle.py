#Q2-In automation, you often compare expected and actual outputs.
#Write code to check if a test case passed or failed.

#expected_title = "Dashboard"
#actual_title = "Dashboard "

#✅ Test Passed – Title matches


#True - why >  Strip and convert them into the lowercase = both of them are equal.

#expected_title ="Dashboard"
#actual_title ="dashboard"

actual_title= input("Enter the actual title \n")
expected_title=input("Enter the expected title \n");

if expected_title.strip().lower() == actual_title.strip():
    print("The Test passed- The title matches")
else:
    print("The Test Failed -The title does not match")

