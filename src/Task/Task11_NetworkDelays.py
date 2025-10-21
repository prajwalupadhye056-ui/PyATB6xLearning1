"""
Question 2 :
An API sometimes fails due to network delays.
Write a program to retry the API call 3 times until the response code becomes 200.
If it still fails after 3 tries, print a failure message.

Hint: Use a while loop with a counter.

Expected Output Example:
Attempt 1: Response 500
Attempt 2: Response 200
---------------------------
✅ Test Passed
❌ Test Failed
"""

count = 1  # initialization

while count <= 3:  # condition
    res = int(input("Enter the API Response code like (200,201,404,500,503 etc.)"))  # do something
    print(f"Attempt {count}: Response {res}")

    if (res == 200):
        break
    count = count + 1

if res == 200:
    print("✅ Test Passed")
else:
    print("❌ Test Failed")
