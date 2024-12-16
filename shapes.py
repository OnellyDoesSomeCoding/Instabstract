import turtle
import random


class Balls:
    def __init__(self, size: int, color, filled: bool):
        self.size = size
        self.color = color if color != 0 else "random"
        self.filled = filled
        self.location = (0,0)

    def random_location(self):
        self.location = (random.randint(-900, 900), random.randint(-500, 500))

    def random_color(self):
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def random_size(self):
        self.size = random.randint(10, 60)

    def draw(self):
        if self.color == "random":
            self.random_color()
        turtle.penup()
        turtle.goto(self.location)
        turtle.pendown()
        if self.filled:
            turtle.fillcolor(self.color)
            turtle.begin_fill()
        turtle.color(self.color)
        turtle.circle(self.size)
        if self.filled:
            turtle.end_fill()

    def mass_draw(self, times):
        if self.size == 0 and self.color != "random":
            for i in range(times):
                self.random_size()
                self.random_location()
                self.draw()
        if self.size != 0 and self.color == "random":
            for i in range(times):
                self.random_color()
                self.random_location()
                self.draw()
        if self.size == 0 and self.color == "random":
            for i in range(times):
                self.random_size()
                self.random_color()
                self.random_location()
                self.draw()

class Polygons:
    def __init__(self, size: int, sides, color, filled: bool):
        self.size = size
        self.sides = sides
        self.orient = 0
        self.color = color if color != 0 else "random"
        self.filled = filled
        self.location = (0, 0)

    def random_sides(self):
        self.sides = random.randint(3, 6)

    def random_orientation(self):
        self.orient = random.randint(0, 90)
        return self.orient

    def random_location(self):
        self.location = (random.randint(-900, 900), random.randint(-500, 500))

    def random_color(self):
        self.color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

    def random_size(self):
        self.size = random.randint(10, 60)

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orient)
        turtle.color(self.color)
        turtle.pendown()
        if self.filled:
            turtle.fillcolor(self.color)
            turtle.begin_fill()
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360/self.sides)
        turtle.penup()
        turtle.end_fill()
        turtle.color(self.color)

    def mass_draw(self, times):
        if self.sides == 0:
            if self.size == 0 and self.color != "random":
                for i in range(times):
                    self.random_sides()
                    self.random_size()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
            elif self.color == "random" and self.size != 0:
                for i in range(times):
                    self.random_sides()
                    self.random_color()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
            elif self.size == 0 and self.color == "random":
                for i in range(times):
                    self.random_sides()
                    self.random_size()
                    self.random_color()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
        elif self.sides != 0:
            if self.size == 0 and self.color != "random":
                for i in range(times):
                    self.random_size()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
            elif self.color == "random" and self.size != 0:
                for i in range(times):
                    self.random_color()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
            elif self.size == 0 and self.color == "random":
                for i in range(times):
                    self.random_size()
                    self.random_color()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
