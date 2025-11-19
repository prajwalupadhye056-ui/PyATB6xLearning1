class Bank:

    def __init__(self ,account_number, balance):
        self.__account_number=account_number # private
        self.balance=balance #public


    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance=self.balance + amount

    def show_me_account_number(self,is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed")

icici_bank=Bank(986325335,200)
icici_bank.deposit(200)
icici_bank.check_balance()
#print(icici_bank.__account_number)


icici_bank.show_me_account_number(True)

