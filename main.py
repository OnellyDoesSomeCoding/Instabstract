"""
Main part of the code that runs everything
"""

import turtle
import setups

setups.setup("fastest")

turtle.onkey(setups.ask_for_random, "r")
turtle.onkey(setups.ask_for_spiral, "s")
turtle.onkey(setups.ask_for_firework, "f")
turtle.onkey(setups.reset_screen, "x")
turtle.onkey(setups.instant, "z")
turtle.onkey(setups.pensize, "c")
turtle.listen()
turtle.done()
