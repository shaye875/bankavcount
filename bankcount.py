class BankCount:
    def __init__(self,account_holder,initial_balance):
        self.holder = account_holder
        self.balance = initial_balance
    def transfer_funds(self,other_account,amount):
        if other_account.balance >= amount:
            other_account.balance-=amount
            self.balance+=amount
            print("done")
        else:
            print("not inagth")
    def __str__(self):
        return f"the account_holder is {self.holder} the initial_balance is {self.balance}"
