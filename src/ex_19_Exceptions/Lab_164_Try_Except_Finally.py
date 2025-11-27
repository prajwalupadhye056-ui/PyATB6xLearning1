try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b
    print(c)
except TypeError:
     print("Error due to Type error")
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Zero division error")
except IndexError:
    print("Index error")
finally:
    print("Hi ,i will always execute")