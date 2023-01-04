import turtle

SEGMENT_SHAPE_NAME = "circle"
COLOR = "green"
SIZE = 20


class Snake:
    _snake: turtle.Turtle

    def __init__(self):
        self._snake = turtle.Turtle()
        self._snake.shape(SEGMENT_SHAPE_NAME)
        self._snake.color(COLOR)
        self._snake.shapesize(SIZE / 20)
        self._snake.penup()

    def get_snake(self):
        return self._snake
