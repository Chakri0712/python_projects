import numpy as np
from PIL import Image


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
