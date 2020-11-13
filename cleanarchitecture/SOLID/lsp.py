


# Liskov Substitution Principle


# If S is a subtype of T, then objects of T may be replaced with objects of S without altering any of the desirable
 # properties of the program.
 # Subtypes should retain the behavior of the main type.
 # Children should be like their parents for what they inherit.


"""
If you have a vehicle and you can drive it, then the classes inheriting from vehicle is also drivable.

,

if you have a mammal class then animal inheriting from mammal class should also be a mammal.
"""




# Implementation


from abc import ABC, abstractmethod
from typing import List

# class Work(ABC):

#     @abstractmethod
#     def name(self):
#         pass

#     @abstractmethod
#     def drive(self):
#         pass


# class TaxiDriver(Work):

#     def name(self):
#         print('Taxi Driver.')

#     def drive(self):
#         print('Taxi driver drives car.')


# class TruckDriver(Work):

#     def name(self):
#         print('Truck Driver.')

#     def drive(self):
#         print('Truck driver drivers truck.')

# class Pilot(Work):

#     def name(self):
#         print('Pilot.')
    
#     def drive(self):
#         print('Pilot do not drive anything.')


# class Works:

#     def __init__(self, jobs: List):
#         self._jobs = jobs
    
#     def do_work(self):
#         for job in self._jobs:
#             job.name()
#             job.drive()
#             print('----------')


# work = Works([TruckDriver(), TaxiDriver(), Pilot()])
# work.do_work()


# Good

class Work(ABC):

    @abstractmethod
    def name(self):
        pass

class Drive(ABC):

    @abstractmethod
    def drive(self):
        pass


class Fly(ABC):

    @abstractmethod
    def fly(self):
        pass


class TruckDriver(Work, Drive):

    def name(self):
        print('Truck Driver.')
    
    def drive(self):
        print('Truck Driver drives truck.')


class TaxiDriver(Work, Drive):

    def name(self):
        print('Taxi Driver.')

    def drive(self):
        print('Taxi Driver drive taxi.')


class Pilot(Work, Fly):

    def name(self):
        print('Pilot')

    def fly(self):
        print('Pilot flies aeroplane')



class Works:
    
    def __init__(self, jobs: List):
        self._jobs = jobs

    def do_work(self):
        for job in self._jobs:
            job.name()
            if hasattr(job, 'fly'):
                job.fly()
            else:
                job.drive()


works = Works([TruckDriver(), TaxiDriver(), Pilot()])
works.do_work()

 