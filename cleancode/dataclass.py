


# Dataclasses


from dataclasses import dataclass


# @dataclass
# class DataclassCard:
#     name: str
#     rank: int



# d = DataclassCard('john smith', 1)

# print(d)
# print(d.rank)


# Dataclass with function
from typing import Any

@dataclass
class Person:

    name: str
    age: int
    size: Any # can be str or int 


    def get_full_name(self):
        return f'Person name: {self.name}, age: {self.age} and size: {self.size}'


person1 = Person('john Cena', 21, '5.6ft')
print(person1.get_full_name())


# Immutable dataclass
from typing import List

@dataclass(frozen=True)
class ImmutableMe:
    name: str
    collections: List[int]


d = ImmutableMe(1,[1,2,3,4])

#outputs errors
# d.name = 2

# do not output errors
d.collections[1] = 10
print(d.collections)

