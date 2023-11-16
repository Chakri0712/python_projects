import numpy as np
from PIL import Image, ImageDraw


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # create a numpy array of zeroes
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # change the zeroes to color provided
        self.data[:] = self.color

    def make(self, image_path):
        image = Image.fromarray(self.data, "RGB")
        # image = Image.new("RGB", (self.height, self.width), self.color)
        # draw = ImageDraw.Draw(image)
        # draw.rectangle((100, 100, 200, 200), fill="blue")
        image.save(image_path)


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y:self.y + self.side] = self.color
        canvas.make("Image.png")


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y:self.y + self.width] = self.color
        canvas.make("Image.png")


canvas_width = int(input("Enter the width of Canvas: "))
canvas_height = int(input("Enter the height of Canvas: "))
canvas = Canvas(500, 500, [200, 20, 20])
# canvas = Canvas(5000, 5000, "Red")
canvas.make("Image.png")
square = Square(100, 150, 75, [50, 50, 200])
square.draw(canvas)
rect = Rectangle(200, 300, 50, 75, [0, 250, 50])
rect.draw(canvas)

# ask user for canvas width, height, color in list format (RGB)
#
# if user chooses square, then ask for x, y, side, color in list format (RGB)
#
# if user chooses rect, then ask for x, y, width, height, color in list format (RGB)

