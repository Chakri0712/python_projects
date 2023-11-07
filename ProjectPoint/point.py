from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        print(self)
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle1):
        if rectangle1.point1.x < self.x < rectangle1.point2.x \
                and rectangle1.point1.y < self.y < rectangle1.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
            (self.point2.y - self.point1.y)


x_min = randint(10, 20)
y_min = randint(10, 20)
x_max = randint(60, 100)
y_max = randint(60, 100)
# Create rectangle object

# rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
#                       Point(randint(10, 19), randint(10, 19)))

rectangle = Rectangle(Point(x_min, y_min),
                      Point(x_max, y_max))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
if user_point.falls_in_rectangle(rectangle):
    print("Your point was inside rectangle")
else:
    print("Your point was not inside rectangle")

print("Your area was off by: ", rectangle.area() - user_area)

t = turtle.Turtle()
t.speed(3)  # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.forward(x_max-x_min)
t.left(90)
t.forward(y_max-y_min)
t.left(90)
t.forward(x_max-x_min)
t.left(90)
t.forward(y_max-y_min)

value = input("enter to close")
