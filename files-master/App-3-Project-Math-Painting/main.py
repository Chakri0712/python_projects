import numpy as np
from PIL import Image, ImageDraw


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self, image_path):
        # data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # data[:] = self.color
        # image = Image.fromarray(data, "RGB")
        image = Image.new("RGB", (self.height, self.width), self.color)
        draw = ImageDraw.Draw(image)
        draw.rectangle((100, 100, 200, 200), fill="blue")
        image.save(image_path)


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        pass


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        pass


# canvas = Canvas(5000, 5000, [200, 20, 20])
canvas = Canvas(5000, 5000, "Red")
canvas.make("Image.png")
