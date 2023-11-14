import numpy as np
from PIL import Image

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [250, 50, 50]

print(data)

data[0:5, 0:3] = [0, 150, 250]

image = Image.fromarray(data, "RGB")
# image.save("image.png")