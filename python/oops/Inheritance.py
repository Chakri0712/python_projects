"""Inheritance is the process by which a class can inherit or derive the properties(or data) and methods(or
functions) of another class. Simply, the process of inheriting the properties of a parent class into a child class is
known as inheritance.

The class whose properties are inherited is the Parent class, and the class that inherits the properties from the
Parent class is the Child class."""


class ParentClass:  # Use CamelCase for class names
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def description(self):
        print(f"Hey! My name is {self.name}, I'm a {self.gender} and I'm {self.age} years old")


class Boy(ParentClass):  # Use CamelCase for class names
    def school_name(self, school_name):  # Use snake_case for method names
        print(f"I study in {school_name}")


# Creating an instance of the Boy class
b = Boy('John', 15, 'male')

# Calling methods from both parent and child classes
b.description()
b.school_name("Sunshine Model School")

"""The super() function in python is a inheritance-related function that refers to the parent class. We can use it to 
find the method with a particular name in an object’s superclass."""


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def description(self):
        print(f"Hey! My name is {self.name}, I'm a {self.gender} and I'm {self.age} years old")

    def dance(self):
        print("I can dance")


class Girl(Human):
    def dance(self):
        print("I can do classic dance")

    def activity(self):
        super().dance()


# Creating an instance of the Girl class
g = Girl('Lily', 20, 'girl')

# Calling methods from the Human and Girl classes
g.description()
g.activity()
