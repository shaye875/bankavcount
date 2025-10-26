from bankcount import *

bank1 = BankCount("avi",100)
bank2 = BankCount("shaye",200)
print(bank1)
print(bank2)
bank2.transfer_funds(bank1,100)
print(bank1)
print(bank2)
