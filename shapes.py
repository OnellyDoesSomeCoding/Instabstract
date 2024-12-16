"""
This file contains 4 objects;
Balls, Polygons, Spiral, Firework
"""

import turtle
import random
import math


class Balls:
    """
    Mutable Balls Object for drawing balls.
    """
    def __init__(self, size: int, color, filled: bool):
        """
        :param size:
        :param color:
        :param filled:
        """
        self.size = size
        self.color = color if color != 0 else "random"
        self.filled = filled
        self.location = (0, 0)

    def random_location(self):
        """
        Randomize Location
        """
        self.location = (random.randint(-900, 900), random.randint(-500, 500))

    def random_color(self):
        """
        Randomize Color
        """
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def random_size(self):
        """
        Randomize Size
        """
        self.size = random.randint(10, 60)

    def draw(self):
        """
        Draw a ball
        """
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
        """
        Draw a number of balls
        """
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
    """
    Mutable Polygons Object for drawing polygons.
    """
    def __init__(self, size: int, sides, color, filled: bool):
        """
        :param size:
        :param sides:
        :param color:
        :param filled:
        """
        self.size = size
        self.sides = sides
        self.orient = 0
        self.color = color if color != 0 else "random"
        self.filled = filled
        self.location = (0, 0)

    def random_sides(self):
        """
        Randomize Sides
        """
        self.sides = random.randint(3, 6)

    def random_orientation(self):
        """
        Randomize Orientation
        """
        self.orient = random.randint(0, 90)
        return self.orient

    def random_location(self):
        """
        Randomize Location
        """
        self.location = (random.randint(-900, 900), random.randint(-500, 500))

    def random_color(self):
        """
        Randomize Color
        """
        self.color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))

    def random_size(self):
        """
        Randomize Size
        """
        self.size = random.randint(10, 60)

    def crude_draw(self):
        """
        Draw a polygon without moving locations
        """
        turtle.setheading(self.orient)
        turtle.color(self.color)
        if self.filled:
            turtle.fillcolor(self.color)
            turtle.begin_fill()
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360 / self.sides)
        turtle.end_fill()

    def draw(self):
        """
        Draw a polygon
        """
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
        """
        Draw a number of polygons
        """
        if self.sides == 0:
            if self.size == 0 and self.color != "random":
                for _ in range(times):
                    self.random_sides()
                    self.random_size()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
            elif self.color == "random" and self.size != 0:
                for _ in range(times):
                    self.random_sides()
                    self.random_color()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
            elif self.size == 0 and self.color == "random":
                for _ in range(times):
                    self.random_sides()
                    self.random_size()
                    self.random_color()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
        elif self.sides != 0:
            if self.size == 0 and self.color != "random":
                for _ in range(times):
                    self.random_size()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
            elif self.color == "random" and self.size != 0:
                for _ in range(times):
                    self.random_color()
                    self.random_location()
                    self.random_orientation()
                    self.draw()
            elif self.size == 0 and self.color == "random":
                for _ in range(times):
                    self.random_size()
                    self.random_color()
                    self.random_location()
                    self.random_orientation()
                    self.draw()


class Spiral(Polygons):
    """
    Spiral object that is made up of polygons and balls
    """
    def __init__(self, size: int, color, filled: bool, sides=4):
        """
        :param size:
        :param color:
        :param filled:
        :param sides:
        """
        super().__init__(size, sides, color, filled)
        self.orient = 0

    def draw_ball_goto(self, x, y):
        """
        :param x:
        :param y:
        Draw a ball at a spot
        """
        turtle.penup()
        turtle.goto(x, y - self.size)
        turtle.pendown()

        if self.filled:
            turtle.fillcolor(self.color)
            turtle.begin_fill()
        turtle.color(self.color)
        turtle.circle(self.size)
        if self.filled:
            turtle.end_fill()

    def draw_poly_goto(self, x, y):
        """
        :param x:
        :param y:
        Draw a polygon at a spot
        """
        turtle.penup()
        turtle.goto(x, y - self.size)
        turtle.setheading(self.orient)
        turtle.pendown()

        if self.filled:
            turtle.fillcolor(self.color)
            turtle.begin_fill()
        turtle.color(self.color)
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360 / self.sides)
        if self.filled:
            turtle.end_fill()

    def draw_ball_spiral(self, times, angle_increment, distance_increment):
        """
        :param times:
        :param angle_increment:
        :param distance_increment:
        Draw a spiral of balls
        """
        if self.size == 0 and self.color != "random":
            for i in range(times):
                self.random_size()
                angle = i * angle_increment
                distance = i * distance_increment
                x = self.location[0] + distance * math.cos(angle)
                y = self.location[1] + distance * math.sin(angle)
                self.draw_ball_goto(x, y)
        if self.size != 0 and self.color == "random":
            for i in range(times):
                self.random_color()
                angle = i * angle_increment
                distance = i * distance_increment
                x = self.location[0] + distance * math.cos(angle)
                y = self.location[1] + distance * math.sin(angle)
                self.draw_ball_goto(x, y)
        if self.size == 0 and self.color == "random":
            for i in range(times):
                self.random_size()
                self.random_color()
                angle = i * angle_increment
                distance = i * distance_increment
                x = self.location[0] + distance * math.cos(angle)
                y = self.location[1] + distance * math.sin(angle)
                self.draw_ball_goto(x, y)

    def draw_poly_spiral(self, times, angle_increment, distance_increment):
        """
        :param times:
        :param angle_increment:
        :param distance_increment:
        Draw a spiral of balls
        """
        if self.size == 0 and self.color != "random":
            for i in range(times):
                self.random_size()
                angle = i * angle_increment
                distance = i * distance_increment
                x = self.location[0] + distance * math.cos(angle)
                y = self.location[1] + distance * math.sin(angle)
                self.draw_poly_goto(x, y)
        if self.size != 0 and self.color == "random":
            for i in range(times):
                self.random_color()
                angle = i * angle_increment
                distance = i * distance_increment
                x = self.location[0] + distance * math.cos(angle)
                y = self.location[1] + distance * math.sin(angle)
                self.draw_poly_goto(x, y)
        if self.size == 0 and self.color == "random":
            for i in range(times):
                self.random_size()
                self.random_color()
                angle = i * angle_increment
                distance = i * distance_increment
                x = self.location[0] + distance * math.cos(angle)
                y = self.location[1] + distance * math.sin(angle)
                self.draw_poly_goto(x, y)
        if self.sides == 0:
            if self.size == 0 and self.color != "random":
                for i in range(times):
                    self.random_sides()
                    self.random_size()
                    self.random_orientation()
                    angle = i * angle_increment
                    distance = i * distance_increment
                    x = self.location[0] + distance * math.cos(angle)
                    y = self.location[1] + distance * math.sin(angle)
                    self.draw_poly_goto(x, y)
            elif self.color == "random" and self.size != 0:
                for i in range(times):
                    self.random_sides()
                    self.random_color()
                    self.random_orientation()
                    angle = i * angle_increment
                    distance = i * distance_increment
                    x = self.location[0] + distance * math.cos(angle)
                    y = self.location[1] + distance * math.sin(angle)
                    self.draw_poly_goto(x, y)
            elif self.size == 0 and self.color == "random":
                for i in range(times):
                    self.random_sides()
                    self.random_size()
                    self.random_color()
                    self.random_orientation()
                    angle = i * angle_increment
                    distance = i * distance_increment
                    x = self.location[0] + distance * math.cos(angle)
                    y = self.location[1] + distance * math.sin(angle)
                    self.draw_poly_goto(x, y)
        elif self.sides != 0:
            if self.size == 0 and self.color != "random":
                for i in range(times):
                    self.random_size()
                    self.random_orientation()
                    angle = i * angle_increment
                    distance = i * distance_increment
                    x = self.location[0] + distance * math.cos(angle)
                    y = self.location[1] + distance * math.sin(angle)
                    self.draw_poly_goto(x, y)
            elif self.color == "random" and self.size != 0:
                for i in range(times):
                    self.random_color()
                    self.random_orientation()
                    angle = i * angle_increment
                    distance = i * distance_increment
                    x = self.location[0] + distance * math.cos(angle)
                    y = self.location[1] + distance * math.sin(angle)
                    self.draw_poly_goto(x, y)
            elif self.size == 0 and self.color == "random":
                for i in range(times):
                    self.random_size()
                    self.random_color()
                    self.random_orientation()
                    angle = i * angle_increment
                    distance = i * distance_increment
                    x = self.location[0] + distance * math.cos(angle)
                    y = self.location[1] + distance * math.sin(angle)
                    self.draw_poly_goto(x, y)


class Firework:
    """
    Firework object for one fire work only
    """
    def __init__(self, color, strands):
        """
        :param color:
        :param strands:
        """
        self.location = (0, 0)
        self.color = color
        self.strands = strands

    def random_color(self):
        """
        Randomize Color
        """
        self.color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        turtle.color(self.color)

    def goto_location(self):
        """
        Go to a location
        """
        turtle.penup()
        turtle.goto(self.location)
        turtle.pendown()

    def random_location(self):
        """
        Randomize Location
        """
        x1, y1 = turtle.screensize()
        x2 = -x1
        y2 = -y1
        self.location = (random.randint(x2, x1), random.randint(y2, y1))

    def create_random(self, length):
        """
        :param length:
        Create a random firework
        """
        random_colors = self.color == 0

        for _ in range(self.strands):
            self.goto_location()

            angle = random.uniform(0, 360)
            turtle.setheading(angle)

            self.create_branching_strand(random_colors, length)

    def create_branching_strand(self, random_colors, length):
        """
        :param random_colors:
        :param length:
        Create a branch of a firework
        """
        for _ in range(random.randint(2, 3)):
            turtle.penup()
            turtle.goto(turtle.xcor(), turtle.ycor())
            turtle.setheading(turtle.heading() + random.randint(-45, 45))
            turtle.pendown()

            if random_colors:
                self.random_color()
            else:
                turtle.color(self.color)

            strands_len = random.randint(length - 30, length + 30)
            turtle.forward(strands_len)

            if random.choice([True, False]):
                turtle.circle(random.randint(10, 30), random.randint(30, 90))
