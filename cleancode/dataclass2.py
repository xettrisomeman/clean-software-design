

# 12 examples of how to write bettter code using @dataclass

from dataclasses import dataclass, field
from typing import List


"""
@dataclass
class Book:
    name: str
    price: int
    condition: str
    weight: float = field(init=False) # dont initlize weight method, user cannot input weight value
    chapters: List[str] = field(default_factory=list)

    # auto intialized weight here
    def __post_init__(self):
        if self.price > 300:
            self.weight = 12.01
        else:
            self.weight = 1.0


book = Book(name= 'To kill a mockingbird', price=300, condition='brand new'
           ,chapters=[1,10,20,30,50,100])
print(book.weight)
"""



# Practical use case

# Suppose a Vat is 10% and Import Tax is 25%
# Then calculate nepali price of goods imported from usd
# get user input too..
# Use dataclasses


@dataclass
class CalculatePrice:
    good_name: str
    price: int
    conversion_rate: int 
    import_tax: int = field(default= 25/100, init=False)
    vat: float = field(default= 15/100, init=False)
    total_cost: int = field(init=False)


    def __post_init__(self):
        cost_after_tax = self.price * self.import_tax
        cost_after_vat = cost_after_tax * self.vat
        total_cost = round((self.price + cost_after_tax + cost_after_vat) * self.conversion_rate,0) # Round to the nearest zero
        self.total_cost = f'{total_cost} Rupees.'
        return self.total_cost


rtxGpu = CalculatePrice('RTX 3090TI', 1500, 118)
print(rtxGpu.total_cost)

# THIS SPARKS JOY

