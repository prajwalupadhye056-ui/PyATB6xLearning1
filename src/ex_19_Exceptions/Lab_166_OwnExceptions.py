def vwo_login(user):
    if user != "admin":
        raise Exception("Unauthorized access!!!")
    return "Welcome"
# print(vwo_login("pramod"))

print(vwo_login("admin"))
