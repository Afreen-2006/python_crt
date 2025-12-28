class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def debit(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"{amount}is debited,bal is {self.getbal()}")
        else:
            print("insuffient balance")
    def credit(self,amount):
            self.balance+=amount
            print(f"{amount}is credited,bal is {self.getbal()}")
    def getbal(self):
        return self.balance
Acc1=Account(1000,"asggffd")
Acc1.credit(500)
Acc1.debit(1000)
                    