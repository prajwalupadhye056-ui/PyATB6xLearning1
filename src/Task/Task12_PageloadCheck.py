"""
Question 3 :

Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.

"""

wait_time = 1

while wait_time <= 5:
    res = input("Is page loaded? (True/False): ")

    if res == "True":
        print("The page is loaded in", wait_time, "seconds")
        break

    wait_time = wait_time+1
else:
    print("Timeout! Page failed to load within 5 seconds")