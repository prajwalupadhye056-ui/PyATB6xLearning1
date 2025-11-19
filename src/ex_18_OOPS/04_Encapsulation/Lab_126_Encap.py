class Car:

    def __init__(self,o_name,o_model,o_make):
        self.name=o_name
        self.model=o_model
        self.make=o_make


    def start_engine(self):
        print("Starting with the car name " + self.name)
        print("Starting with the model " + self.model)
        print("Starting with the make " + self.make)

lambo = Car("lambo","2025","V6")
lambo.start_engine()

mg_hector = Car("mg_hector","2025", "BN")
mg_hector.start_engine()
