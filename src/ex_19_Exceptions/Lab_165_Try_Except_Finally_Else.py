try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b

except TypeError:
     print("Error due to Type error")
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Zero division error")
except IndexError:
    print("Index error")
else:  # Runs only when try block succeeds
    print(c)
finally:
    print("Hi ,i will always execute")