




# Design principle - SOLID

"""

The SOLID principles tell us how to arrange our functions and data structures
into classes, and how those classes should be interconnected.

# A class is simply a coupled grouping of functions and data.

"""

# SOLID

# SRP -> The single Responsibility principle
# OCP -> The open-close principle
# LSP -> The liskov substitution principle
# ISP -> The Interface segregation principle
# DIP -> The dependency Inversion Principle

"""
1) SRP -> A class should have one, and only one, reason to change.(Should focus on single task)
-> Very precies names for many small classes
-> generic names for large classes
-> Find one reason to change and take everything out from the class.

"""

# NOT SRP
# This violates SRP because class doing different things.

# class Invoice:

#     def __init__(self, customer, state, total):
#         self.customer = customer
#         self.state = state
#         self.total = total

    
#     def details(self):
#         return f'Customer {self.customer}, Total: {self.total}'

#     def sales_tax(self):
#         if self.state == 'AZ':
#             return 5.5
#         elif self.state == 'TX':
#             return 3.2
#         elif self.state == 'CA':
#             return 8.7

#     def email_invoice(self):
#         print('Emailing invoice')
#         print(self.details())



# invoice = Invoice('Google', "AZ", 100)
# print(invoice.sales_tax())
# invoice.email_invoice()

# 5.5
# Emailing Invoice
# Customer: Google, Total:100

# SRP


class Invoice:

    def __init__(self, customer, total):
        self.customer = customer
        self.total = total

    def details(self):
        return f'Customer: {self.customer}, Total: {self.total}'


class SalesTax:

    def __init__(self, state):
        self.state = state

    def calculate_tax(self):
        if self.state == 'AZ':
            return 5.5
        elif self.state == "CA":
            return 8.7
        elif self.state == 'TX':
            return 3.2


class Email:

    def send_email(self, content):
        print('Emailing')
        print(content)


invoice = Invoice('Google', 100)
tax = SalesTax('CA')
print(tax.calculate_tax())
Email().send_email(invoice.details())

