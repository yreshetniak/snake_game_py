import turtle

OBJECT_SHAPE_COORDINATES = ((0, 0), (10, 10), (20, 0), (10, -10))
SHAPE_NAME = "diamond"
COLOR = "blue"
SIZE = 20


class Food:
    _food: turtle.Turtle

    def __init__(self):
        self._food = turtle.Turtle()
        # registering the new shape
        turtle.register_shape(SHAPE_NAME, OBJECT_SHAPE_COORDINATES)

        self._food.shape(SHAPE_NAME)
        self._food.color(COLOR)
        self._food.shapesize(SIZE / 20)
        self._food.penup()

    def get_food(self):
        return self._food
