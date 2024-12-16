![UML](uml_instabstract.png)
# UML For Instabstract

Instabstract is an Object Oriented Program that aims to create "modern art," If you've seen the internet recently, modern art has been filled to the brim with slop content, for example: Concetto spaziale, Attesse by Lucio Fontana, selling at a peak of 1.2 million US Dollar, which to a normal person, is extremely absurb and nonsensical. So, I had a thought, if these so-called artist could do it, how come--a normal person like me--couldn't.

This is the start of my project, Instabstract with 3 options to pick from. Imagination is the limit.

# How to install

- Install shapes.py, setups.py, and main.py
- Make sure you have python installed too.
- Start by running each of the file, be sure to put the file in the same folder on the same directory for it to work.

# Usage

The program is aim to revolutionize the "modern art" industry by being able to create abstract pieces of art by just simple buttons. The expected outputs would be a finished picture, created by turtle, and consisting of many shapes and colors. To use the program, just press keys on your keyboard, such as; R key for a random pattern to be generated, using your choice of colors and shapes.

Here is my YouTube Link to the demo; https://youtu.be/Whmd-w7tXQk

# Project Design

The Balls and Polygon class are just the base shape that could be draw directly, or be used as a superclass for other classes. Spiral, using Polygon as it's superclass, is a class that is made for creating Balls and Polygons into patterns of spirals; using Trigonometry to calculate the distance and angle of each shapes drawn. And Firework class represents each firework that could be draw with lines created by turtle, implementing similar trigonometry functions with Spiral class.

I've extended a previous assignment, Week 12. It is what pathfinded my project and to make the old assignment better by implementing all sorts of other functions, like event-based programming for each of the choices, and also implementing other turtle functions that I've never used in other assignments.

The code works by having normal subroutine functions to get an return values to be assigned into the classes of shapes and patterns before running them directly in the subroutine functions, by this you could create multiple randomly generated shapes from the classes. I think 90% of my code is working completely, there are some flaws; when you try to generate two patterns in the same canvas, sometimes it doesn't work. To be completely honest, it had been a problem since I implemented anything in the first place and I sincerely apologize for not having a fix to this problem, any advice would be appreciated. One more problem is with Pylinting, it notifies E1101 on every line with turtle somehow, Ignoring that and my files will be almost 100% Clean.

# Possible Upcoming Features

I would like to implement other shapes, or maybe to change the backgrounds. I also would like to make a "framing" system for people to name their created art and save it to their device and maybe sell it as an NFT or a physical piece of art.

# Notes

I give myself a 90 in Sophistication Level, because one of my major flaws in this project is not implementing physical parts of the program like instructed in class. Still, I hope you enjoy this project and maybe sell some of my "modern arts" for a few million dollar!
