import random
import turtle
import shapes

def pensize():
    size = int(input(">>>"))
    turtle.pensize(size)

def setup(speed):
    turtle.hideturtle()
    turtle.speed(speed)
    turtle.colormode(255)
    turtle.bgcolor("black")

    print('''
░█──░█ █▀▀ █── █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ▀█▀ █▀▀▄ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀▄ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀ ▀▀█▀▀ 
░█░█░█ █▀▀ █── █── █──█ █─▀─█ █▀▀ 　 ─░█── █──█ 　 ░█─ █──█ ▀▀█ ──█── █▄▄█ █▀▀▄ ▀▀█ ──█── █▄▄▀ █▄▄█ █── ──█── 
░█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀───▀ ▀▀▀ 　 ─░█── ▀▀▀▀ 　 ▄█▄ ▀──▀ ▀▀▀ ──▀── ▀──▀ ▀▀▀─ ▀▀▀ ──▀── ▀─▀▀ ▀──▀ ▀▀▀ ──▀──

[?] Press R on your keyboard to start generating random patterns
[?] Press S on your keyboard to start generating spiral patterns
[?] Press F on your keyboard to start generating fireworks

[!] Press Z for the art to finish instantly
[!] Press X on your keyboard to clear the screen (This only works when the art is finished)
[!] Press C on your keyboard to change the size of the pen, would be present as an input option

=============================================================================================================
''')

def reset_screen():
    turtle.clear()

def instant():
    turtle.tracer(0)

def get_color():
    print("[?] We're currently using RGB Code, The range is between 0 to 255. We shall proceed.")
    while True:
        r = int(input("> R Code : "))
        g = int(input("> G Code : "))
        b = int(input("> B Code : "))
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            c = tuple((r, g, b))
            return c
        else:
            print("[!] Repeat. We're currently using RGB Code, The range is between 0 to 255.")

def get_parameter(item: str):
    while True:
        size = int(input(f'''> How big do you want your {item} to be? 0 for random. (Should be about 10 to 60)
        Answer : '''))
        if size < 0:
            print("[!] Please provide a suitable answer.")
        else:
            break

    while True:
        color = int(input('''> Do you want the colors to be randomized?
        1. Yes
        2. No
        Answer : '''))
        if color == 1:
            color = 0
            break
        elif color == 2:
            color = get_color()
            break
        else:
            print("[!] Please provide a suitable answer.")

    while True:
        choice_fb = int(input(f'''> Do you want your {item} to be filled?
        1. Yes
        2. No
        Answer : '''))
        if choice_fb == 1:
            choice_fb = True
            break
        elif choice_fb == 2:
            choice_fb = False
            break
        else:
            print("[!] Please provide a suitable answer.")

    return size, color, choice_fb

# Name suggests
def ask_for_random():
    while True:
        ball_yes = int(input('''Do you want balls?
        1. Yes
        2. No
        Answer : '''))
        if ball_yes == 1:
            ball_size, ball_color, ball_choice = get_parameter("Balls")
            case_ball = shapes.Balls(ball_size, ball_color, ball_choice)
            break
        elif ball_yes == 2:
            break
        else:
            print("[!] Please provide a suitable answer.")

    while True:
        poly_yes = int(input('''Do you want polygons?
        1. Yes
        2. No
        Answer : '''))
        if poly_yes == 1:
            poly_size, poly_color, poly_choice = get_parameter("Polygons")
            while True:
                sides = int(input("> How many sides do you want? 0 for random.\n        Answer : "))
                if sides >= 3 or sides == 0:
                    break
                else:
                    print("[!] Please provide a suitable answer.")
            case_poly = shapes.Polygons(poly_size, sides, poly_color, poly_choice)
            break
        elif poly_yes == 2:
            break
        else:
            print("[!] Please provide a suitable answer.")

    while True:
        random_amount = int(input("How many shapes do you want? 0 for random. \
 (Should be in the hundreds for best result)\n        Answer : "))
        if random_amount == 0:
            times = random.randint(100,300)
            break
        elif random_amount > 0:
            times = random_amount
            break
        else:
            print("[!] Please provide a suitable answer.")

    if ball_yes == 1 and poly_yes == 2:
        case_ball.mass_draw(times)
    elif ball_yes == 2 and poly_yes == 1:
        case_poly.mass_draw(times)
    elif ball_yes == 1 and poly_yes == 1:
        case_ball.mass_draw(times)
        case_poly.mass_draw(times)

# Name suggests
def ask_for_spiral():
    while True:
        what_shape = int(input('''What shapes do you want as your spiral?
        1. Balls
        2. Polygons
        Answer : '''))
        if what_shape == 1:
            size, color, filled = get_parameter("Balls")
            spiral_ball = shapes.Spiral(size, color, filled, 0)
            break
        elif what_shape == 2:
            size, color, filled = get_parameter("Polygons")
            while True:
                sides = int(input("> How many sides do you want? 0 for random.\n        Answer : "))
                if sides >= 3:
                    break
                elif sides == 0:
                    sides = random.randint(3,6)
                    break
                else:
                    print("[!] Please provide a suitable answer.")
            spiral_poly = shapes.Spiral(size, color, filled, sides)
            break
        else:
            print("[!] Please provide a suitable answer.")

    while True:
        random_amount = int(input("How many shapes do you want? 0 for random. \
 (Should be in the hundreds for best result)\n        Answer : "))
        if random_amount == 0:
            times = random.randint(100,300)
            break
        if random_amount > 0:
            times = random_amount
            break
        else:
            print("[!] Please provide a suitable answer.")

    while True:
        random_angle = int(input("What angle increment do you want? 0 for random. \
 (Should be about 10 to 20 for best result)\n        Answer : "))
        if random_angle == 0:
            angle_inc = random.randint(15,90)
            break
        elif random_angle > 0:
            angle_inc = random_angle
            break
        else:
            print("[!] Please provide a suitable answer.")

    while True:
        random_distance = int(input("How much distance do you want? 0 for random. \
 (Should be lesser than 10 for best result)\n        Answer : "))
        if random_distance == 0:
            distance_inc = random.randint(3,5)
            break
        elif random_distance > 0:
            distance_inc = random_distance
            break
        else:
            print("[!] Please provide a suitable answer.")

    if what_shape == 1:
        spiral_ball.draw_ball_spiral(times, angle_inc, distance_inc)
    elif what_shape == 2:
        spiral_poly.draw_poly_spiral(times, angle_inc, distance_inc)

# Name suggests
def ask_for_firework():
    while True:
        color = int(input('''> Do you want the colors to be randomized?
        1. Yes
        2. No
        Answer : '''))
        if color == 1:
            color = 0
            break
        elif color == 2:
            color = get_color()
            break
        else:
            print("[!] Please provide a suitable answer.")

    while True:
        strands = int(input('''> How many strands do you want? 0 for random.
        Answer : '''))
        if strands == 0:
            strands = random.randint(8,15)
            break
        elif strands > 0:
            break
        else:
            print("[!] Please provide a suitable answer.")

    while True:
        length = int(input('''> How long do you want the strands to be? 0 for random.
        Answer : '''))
        if length == 0:
            length = random.randint(8,15)
            break
        elif length > 0:
            break
        else:
            print("[!] Please provide a suitable answer.")

    while True:
        amount = int(input('''> How many fireworks do you want? 0 for random.
        Answer : '''))
        if amount == 0:
            amount = random.randint(4,8)
            break
        elif amount > 0:
            break
        else:
            print("[!] Please provide a suitable answer.")

    for i in range(amount):
        fire = shapes.Firework(color, strands)
        fire.random_location()
        fire.create_random(length)
