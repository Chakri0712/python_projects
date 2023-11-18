from canvas import Canvas
from shapes import Square, Rectangle

canvas_width = int(input("Enter the width of Canvas: "))
canvas_height = int(input("Enter the height of Canvas: "))
canvas_color_dict = {"white": [255, 255, 255], "Black": [0, 0, 0]}
canvas_color = input("select the color of canvas Black or White: ")


def draw_req_shape(canvas):
    while True:
        shape = input("What do you want to draw? Rectangle or Square. Type something else to quit the game: ")
        if shape.lower() == "rectangle":
            x_coordinate = int(input("Enter X coordinate: "))
            y_coordinate = int(input("Enter Y coordinate: "))
            rect_width = int(input("Enter the width of Rectangle: "))
            rect_height = int(input("Enter the height of Rectangle: "))
            rect_color_input = input("Enter values of RGB separated by spaces: ")
            rect_color = [int(element) for element in rect_color_input.split()]
            rect = Rectangle(x_coordinate, y_coordinate, rect_width, rect_height, rect_color)
            rect.draw(canvas)
        elif shape.lower() == "square":
            x_coordinate = int(input("Enter X coordinate: "))
            y_coordinate = int(input("Enter Y coordinate: "))
            square_side = int(input("Enter the side of Square: "))
            square_color_input = input("Enter values of RGB separated by spaces: ")
            square_color = [int(element) for element in square_color_input.split()]
            square = Square(x_coordinate, y_coordinate, square_side, square_color)
            square.draw(canvas)
        else:
            break


def make_shape(color):
    canvas = Canvas(canvas_width, canvas_height, canvas_color_dict[color])
    canvas.make("Image.png")
    draw_req_shape(canvas)


if canvas_color.lower() == "white":
    make_shape("white")
elif canvas_color.lower() == "black":
    make_shape("Black")

# canvas = Canvas(5000, 5000, "Red")
