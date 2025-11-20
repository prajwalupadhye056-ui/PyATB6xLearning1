class Father1:
    def money(self):
        print("F1 money")

class Father2:
    def money(self):
        print("F2 money")

class Child(Father1, Father2):
    def give_money(self):
        print("Son")
        self.money()

tc2= Child()
tc2.give_money()
