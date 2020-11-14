

# Dependency Inversion Principle



"""
The Dependency Inversion Principle tells us that the most flexible systems are those in which source code
dependencies refer only to abstractions, not to concretions.
"""

# Abstractions should not depend on details. Details should depend on abstractions


# Implementation

from random import choice

# class Book:

#     def __init__(self):
#         self.books = ["Nausea", "The Stranger", "The Myth Of Sisyphus", "Deep Learning", "1984", "Dune"]

#     def get_book(self):
#         choices = choice(self.books)
#         return choices


# class Library:

#     def __init__(self):
#         self.book = Book()

#     def read_book(self):
#         print(f"Reading : {self.book.get_book()}")


# library = Library()
# library.read_book()



# using DIP

class Book:

    def __init__(self):
        self.books = ["Nausea", "The Stranger", "The Myth Of Sisyphus", "Deep Learning", "1984", "Dune"]

    def get_book(self):
        choices = choice(self.books)
        return choices


class Library:

    def __init__(self, book): # passing class as a dependency 
        self.book = book()

    def read_book(self):
        print(f"Reading : {self.book.get_book()}")


library = Library(Book)
library.read_book()

