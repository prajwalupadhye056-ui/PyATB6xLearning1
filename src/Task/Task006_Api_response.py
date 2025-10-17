#Q - You receive an API response code from your test script.
#Write an if-else block to check whether the response is successful (status code 200) or not.

#I/P response = 404 , O/P ❌ Failed API Request
#I/P response = 200 , O/P ✅ Passed API Request


response= int(input("Enter the api response \n"))

if response == 200:
    print("Api response is successful")
elif response ==404:
    print("Api response is failed")
else:
    print("Enter valid response code")