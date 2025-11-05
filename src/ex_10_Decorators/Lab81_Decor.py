def before_after_ui_test(func):
    def wrapper():
        print("Before Running code")
        func()
        print("After Running code")

    return wrapper()



@before_after_ui_test
def test_ui():
    print("Hi, I am testing a UI test")