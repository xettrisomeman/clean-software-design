
from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: str
    height: float = field(init= False)

    def __post_init__(self):
        if len(self.name) > 10:
            self.height = 1.75
        else:
            self.height = 1.20
        return True
