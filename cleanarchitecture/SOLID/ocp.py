

# OPEN CLOSED PRINCIPLE

# a software artifact should be open for extentsion but closed for modification.
 # -> change or extend the behavior of a system, without changing any existing code.
 # -> The behavior of a software artifact ought to be extendible, without having to modify that artifact.
 # -> extend behavior without modifying its source code.

# Software entities should not depend on things they do not use.
# Example:- Open Source Library
# should not use lots of if and else in a function

# class OrderReport:

#     def __init__(self, customer, total):
#         self.customer = customer
#         self.total = total

#     def invoice(self):
#         print('Invoice')
#         print(self.customer)
#         print(self.total)

#     def bill_of_loading(self):
#         print('BIL')
#         print(self.customer)
#         print('Shipping Label')

    
# order = OrderReport('Google', 2000)
# order.invoice()
# order.bill_of_loading()

# OCP
# Never rewrite your existing code, only add new code


class OrderReport:

    def __init__(self, customer, total):
        self.customer = customer
        self.total = total
    


class Invoice(OrderReport):

    def invoice(self):
        print('Invoice')
        print(self.customer)
        print(self.total)


class BillOfLading(OrderReport):

    def __init__(self, *args, address):
        super().__init__(*args)
        self.address = address

    def bill_of_lading(self):
        print('BIL')
        print(self.customer)
        print('Shiping Label...')
        print(self.address)


invoice = Invoice('Google', 100)
bill = BillOfLading('Yahoo', 200, address = '123 This street')
invoice.invoice()
bill.bill_of_lading()
