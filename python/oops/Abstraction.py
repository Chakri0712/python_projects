"""
Abstraction in a similar way just shows us the functionalities anything holds, hiding all the implementations

The main goal of Abstraction is to hide background details or any unnecessary implementation about the data so that
users only see the required information. It helps in handling the complexity of the codes.

"""
from abc import ABC

"""
To use abstraction, it is mandatory for us to import ABC class from the abc module.

ABC stands for Abstract Base class. The abc module provides the base for defining Abstract Base classes (ABC).
"""


class Vehicle(ABC):  # inherits abstract class
    # abstract method
    def no_of_wheels(self):
        print("hello")


class Bike(Vehicle):
    def no_of_wheels(self):  # provide definition for abstract method
        print("Bike has 2 wheels")


class Tempo(Vehicle):
    def no_of_wheels(self):  # provide definition for abstract method
        print("Tempo has 3 wheels")


class Truck(Vehicle):
    def no_of_wheels(self):  # provide definition for abstract method
        print("Truck has 4 wheels")


veh = Vehicle()
veh.no_of_wheels()

bike = Bike()
bike.no_of_wheels()

tempo = Tempo()
tempo.no_of_wheels()

truck = Truck()
truck.no_of_wheels()
