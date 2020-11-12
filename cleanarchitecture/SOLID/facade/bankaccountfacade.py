

# Srp is well written with 'facade' pattern.

from accountnumbercheck import AccountNumberCheck
from fundscheck import FundsCheck
from securitycodecheck import SecurityCodeCheck
from welcometobank import WelcomeToBank



class BankAccountFacade:

    def __init__(self, newAcctNum, newSecCode):
        self.__accountNumber = newAcctNum
        self.__securityCode = newSecCode
        self.acctChecker = AccountNumberCheck()
        self.codeChecker = SecurityCodeCheck()
        self.fundChecker = FundsCheck()
        self.bankWelcome = WelcomeToBank()

    def getAccountNumber(self):
        return self.__accountNumber

    def getSecurityCode(self):
        return self.__securityCode

    def withDrawCash(self, cashToGet):
        if self.acctChecker.accountActivation(self.getAccountNumber()) and self.codeChecker.isCodeCorrect(self.getSecurityCode()):
            self.fundChecker.haveEnoughMoney(cashToGet)
            print('Transaction Complete.\n')
        else:
            print('Transaction Failed.\n')

    def depositCash(self, cashToDeposit):
        if self.acctChecker.accountActivation(self.getAccountNumber()) and self.codeChecker.isCodeCorrect(self.getSecurityCode()):
            self.fundChecker.makeDeposit(cashToDeposit)
            print('Transaction Complete.\n')
        else:
            print('Error In Transaction.')

    

def main():
    accessingBank = BankAccountFacade(12345678, 1234)
    accessingBank.withDrawCash(50.00)
    accessingBank.withDrawCash(100.00)
    accessingBank.depositCash(200.00)

main()

