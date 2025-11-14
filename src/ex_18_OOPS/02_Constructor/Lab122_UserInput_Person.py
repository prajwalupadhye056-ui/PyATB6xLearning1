class Person:

    def __init__(self):
        print("Let's take the user input, Please share the name,age ,phone,occupation")
        self.name=input("\nEnter the name \n")
        self.age= input("\n Enter the age\n")
        self.phone =input("\n Enter the phone\n ")
        self.occupation =input("\n Enter the occupation\n")

    def display_values(self):
        print("Name is:", self.name, "Age is:",self.age,"Phone is", self.phone,"Occupation is", self.occupation)


amit =Person()
amit.display_values()