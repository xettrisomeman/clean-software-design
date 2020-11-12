


# Getting something to work once, just isnot that hard.
# Getting it right is another matter.
# Getting software right is hard.
# Requires thoughts and insights.
# Passion for craft and desire to be a professional.
# Getting software right means doing magic. ->
   # You don't need massive documents or huge issue tracking systems.
   # You don't need hordes of programmers to keep it working.

"""
The goal of software architecture is to minimize the human
resources required to build and maintain the required
system.
"""


# Modern devlopers work their butts off. But a part of their brain does sleep.
# (The part that knows that good, clean and well-designed code matters)

# Things never do get cleaned up later, because market pressure never abate.

# Getting to market fast means, we have to stay at first and beat other developers by running as fast as you can.


"""
And so the developers never switch modes. They Can't go back and clean things
up because they have got to get the next feature done, and the next, and
the next , and the next . And so the mess builds, and productivity continues its 
asymptotic approach toward zero.

"""


"""
The bigger lie that developers buy into is the notion
that writing messy code makes them go fast in the short
term, and just slows them down in the long term.
"""

# The only way to go fast is to go well.

# Take responsibility of the code you write.

# Quality of software architecture should be taken seriously.

# Software must be 'soft', means easy to change.



# OOP PRINCIPLE

# Composition vs Inheritance



# Inheritance


# IS A -> inheritance

class Animal:

   def __init__(self, name):
      self.name = name

   def eat(self):
      print(f'{self.name} is eating.')



class Dog(Animal):
   
   def __init__(self, name):
      super().__init__(name)

   def bark(self):
      print(f'{self.name} bark.')


class Cat(Animal):

   def __init__(self, name):
      """This class IS (A) related to animal class"""
      
      
      super().__init__(name)

   
   def meow(self):
      print(f'{self.name} meow.')



dog = Dog('puppy')
cat = Cat('lana')

# dog.eat()
# cat.eat()

# Inheritance creates subclass based on superclass.


# Composition


# HAS A -> composition


class Person:

   def __init__(self, name):
      self.name = name

   def walk(self):
      print(f'{self.name} is walking.')



class Vehicle:

   def __init__(self, vehicle_name):
      self.vehicle = vehicle_name

   
   def move(self):
      print(f'{self.vehicle} is moving.')

   

class Apartment:

   def __init__(self, person_name, vehicle_name):
      """This class HAS A objects relation with Person and vehicle class"""
      self.person = Person(person_name)
      self.vehicle = Vehicle(vehicle_name)

   def move(self):
      return self.vehicle.move()

   def walk(self):
      return self.person.walk()



apartment = Apartment('john cena', 'Tesla v100')

apartment.walk()

