


# Using class instead of def
# Helps to control and manage code easily


# Encapsulation == Information Hiding
# Abastraction == Implementation Hiding
# Polymerphism == One function can be used at any place
# Inheritance == A class can act as parent or derived



class Cpu:

    def __init__(self):
        self.__model = None
        self.__ram = None
        self.__cost = None

    @property
    def data(self):
        print(f'The model is {self.__model} , ram: {self.__ram} and cost : {self.__cost}')
    
    @data.setter
    def data(self, values):
        model, ram, cost = values
        self.__model = model
        self.__ram = ram
        self.__cost = cost


class Gpu:

    def __init__(self):
        self.__model = None
        self.__ram = None
        self.__cost = None

    @property
    def data(self):
        print(f'The model is {self.__model} , ram: {self.__ram} and cost : {self.__cost}')
    
    @data.setter
    def data(self, values):
        model, ram, cost = values
        self.__model = model
        self.__ram = ram
        self.__cost = cost



class Computer:

    def __init__(self):
        self.cpu = Cpu()
        self.gpu = Gpu()

    def addValue(self, types, model, ram, cost):
        if types.lower() == 'gpu':
            self.gpu.data = (model, ram, cost)
            return self.gpu.data
        self.cpu.data = (model, ram, cost)
        return self.cpu.data


def main():
    computer = Computer()
    computer.addValue('gpu', 'RTX 3090TI', '24GB', '1500USD')
    computer.addValue('cpu', 'AMD RYZEN 3900x Threadripper', '48GB', '749USD')


main()

