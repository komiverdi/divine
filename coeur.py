import turtle
import math
import time
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)
screen.tracer(0)

def heart_x(teta):
    return 16 * math.sin(teta) ** 3

def heart_y(teta):
    return (13 * math.cos(teta)
            - 5 * math.cos(2 * teta)
            - 2 * math.cos(3 * teta)
            - math.cos(4 * teta))


SCALE = 10

for i in range(0, 360, 2):
    hue = i / 360.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(r, g, b)

    t.penup()
    t.goto(0, 0)
    t.pendown()

    angle = math.radians(i)
    x = heart_x(angle)
    y = heart_y(angle)

    t.goto(x * SCALE, y * SCALE)

    time.sleep(0.01)
t.penup()
t.color("white")
t.goto(0, 170)
t.write("je t'aime divine !", align="center", font=("Arial", 18, "bold"))

turtle.done()