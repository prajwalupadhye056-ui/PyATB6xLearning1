names = ["TestingAcademy", "", "Pass", "QA","Automation"]
def non_empty(x):
    if x != "":
        return True
    return None

non_empty_List = list(filter(non_empty,names))  #removes empty Strings
print(non_empty_List)