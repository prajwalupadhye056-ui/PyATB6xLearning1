print("Enter the test which you want to  run \n")
test_type= input("Enter the test type : API,UI ,Performance, Security \n")

match test_type:
    case "API":
        print("We are running API test case")

    case "UI":
        print("We are running UI test case")

    case "Performance":
        print("We are running Performance test case")

    case "Security":
        print("We are running Security test case")

    case _:
        print("Invalid case")
"""
        #if else
        test_type=input("Enter the test type :").strip()

        if test_type == "API":
            print("We are running API test case")
        elif test_type == "UI":
            print("We are running UI test case")

        elif test_type == "Performance":
            print("We are running Performance test case")

        elif test_type == "Security":
            print("We are running security test case")
        else :
            print("Invalid type")

   """