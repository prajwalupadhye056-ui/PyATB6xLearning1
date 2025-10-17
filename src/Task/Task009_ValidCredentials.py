#Q4 -Check if the user can log in based on correct username and password.

#I/p

#username = "admin"
#password = "1234"

#O/p
#✅ Login Successful


#For the Fail condition Other O/P = ❌ Invalid Credentials

username= input("Enter the admin credentials \n").strip()
password =input("Enter the password credentials \n").strip()

if username.lower() == "admin" and password == "1234":
    print("login successful")
else:
    print("Invalid credentials")

