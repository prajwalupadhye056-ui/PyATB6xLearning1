pb_global = 12


def my_function():
    pb_a=10
    print(pb_a)
    print(pb_global)

print(pb_a)# not allowed as it is local variable
print(pb_global)
my_function()
