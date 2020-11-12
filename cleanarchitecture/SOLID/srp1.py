


# Single Responsibility Principle


class Email:

    @staticmethod
    def sendMessage(message):
        print(message)



class CashRegister:

    def __init__(self):
        self.subTotal = 0
        self.taxRate = 7.5
        self.grandTotal = 0

    @property
    def get_subTotal(self):
        Email.sendMessage(f'The message has been sent with cost {self.subTotal}')
    
    @get_subTotal.setter
    def get_subTotal(self, subTotal):
        self.subTotal = subTotal

register = CashRegister()

register.get_subTotal = 100
register.get_subTotal

