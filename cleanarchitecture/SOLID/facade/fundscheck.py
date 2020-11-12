class FundsCheck:

    
    def __init__(self):
        self.__cashInAccount = 1000.00


    def getCashInAccount(self):
        return self.__cashInAccount


    def decreaseCashInAccount(self, cashWithdrawn):
        self.__cashInAccount -= cashWithdrawn


    def increaseCashInAccount(self, cashDeposited):
        self.__cashInAccount += cashDeposited


    def haveEnoughMoney(self, cashToWithDrawal):
        if cashToWithDrawal > self.getCashInAccount():
            print('You dont have enough money')
            print(f'Current balance: {self.getCashInAccount()}')
            return False
        else:
            self.decreaseCashInAccount(cashToWithDrawal)
            print(f'Withdrawal Complete: Current Balance is {self.getCashInAccount()}')
            return True
        

    def makeDeposit(self, cashToDeposit):
        self.increaseCashInAccount(cashToDeposit)
        print(f'Deposit Completed:, Current Balance is {self.getCashInAccount()}')




