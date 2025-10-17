# Q3 -You want to check whether a web page loads within 3 seconds (performance test condition).

# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

load_time = float(input("Enter the page load time in seconds \n"))

if load_time <= 0:
    print("⚠️ Invalid input: load time must be greater than 0 seconds")
elif load_time <= 3:
    print(f"✅ Page loaded successfully in {load_time} seconds")
else:
    print(f"⚠️ Page load too slow: {load_time} seconds")
