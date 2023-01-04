import turtle
from turtle import *

WIDTH = 600
HEIGHT = 600
TITLE = "Simplest Snake"
BACKGROUND_COLOR = "#87ADA9"


class GameScreen:
    _width: int
    _height: int
    __instance: Screen

    def __init__(self):
        self._width = WIDTH
        self._height = WIDTH
        self.__init_screen()

    def __init_screen(self):
        self.__instance = turtle.Screen()
        self.__instance.setup(self._width, self._height)  # Set the dimensions of the Turtle Graphics window.
        self.__instance.cv._rootwindow.resizable(False, False)  # Make screen not resizable
        self.__instance.title(TITLE)
        self.__instance.bgcolor(BACKGROUND_COLOR)
        self.__instance.tracer(0)  # Turn off automatic animation.

        # Event handlers
        self.__instance.listen()  # Make screen listen to events like keyboard

    def get_screen(self):
        return self.__instance

    def update_score_in_title(self, score):
        self.__instance.title(f"{TITLE}. Score: {score}")
        self.__instance.update()
