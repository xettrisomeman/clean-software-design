# A module should be responsible to one, and only one, actor.

# Actor -> refer to the group of people or stakeholders

# module -> source file

# Srp says 'to separate the code that diffrent actors depend on'

# Separate code that supports different actors.

# SRP and Facade go hand in hand

class PayCalculator:

    def __init__(self, price):
        self.price = price

    @staticmethod
    def get_price(message):
        print(message)

class HourReporter:

    def __init__(self, hour):
        self.hour = hour

class EmployeeSaver:

    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language


class EmployeeFacade:

    def __init__(self, name, age, language):

        # using facade design pattern

        self.pay = PayCalculator(100)
        self.hour = HourReporter(10)
        self.save = EmployeeSaver(name, age, language)

    def price(self):
        return PayCalculator.get_price(self.pay.price)


employee = EmployeeFacade('samman', 21, 'Python')
employee.price()

