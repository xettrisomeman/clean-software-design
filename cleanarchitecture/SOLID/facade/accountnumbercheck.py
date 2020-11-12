

class AccountNumberCheck:

    
    def __init__(self):
        self.__accountNumber = 12345678

    def getAccountNumber(self):
        return self.__accountNumber

    def accountActivation(self, acctNumToCheck):
        if acctNumToCheck == self.getAccountNumber():
            return True
        else:
            return False

