"""Polymorphism in OOPS refers to the functions having the same names but carrying different functionalities. Or,
having the same function name, but different function signature(parameters passed to the function).

A child class inherits all properties from its parent class methods. But sometimes, it wants to add its own
implementation to the methods. There are ample of ways we can use polymorphism in Python."""


class Monkey:
    def color(self):
        print("The monkey is yellow coloured!")

    def eats(self):
        print("The monkey eats bananas!")


class Rabbit:
    def color(self):
        print("The rabbit is white coloured!")

    def eats(self):
        print("The rabbit eats carrots!")


# Creating instances of the Monkey and Rabbit classes
mon = Monkey()
rab = Rabbit()

# Iterating over a tuple of animals and calling their methods
for animal in (mon, rab):
    animal.color()
    animal.eats()


class Shape:
    def no_of_sides(self):
        pass

    def two_dimensional(self):
        print("I am a 2D object. I am from the Shape class")


class Square(Shape):
    def no_of_sides(self):
        print("I have 4 sides. I am from the Square class")


class Triangle(Shape):
    def no_of_sides(self):
        print("I have 3 sides. I am from the Triangle class")


# Creating an object of the Square class
sq = Square()

# Overriding the no_of_sides method of the parent class
sq.no_of_sides()

# Creating an object of the Triangle class
tr = Triangle()

# Overriding the no_of_sides method of the parent class
tr.no_of_sides()
