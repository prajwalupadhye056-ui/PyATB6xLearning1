count = 0

def increment():
    global count # global -to give global
    count = count +1

increment()
increment()
increment()
print(count)