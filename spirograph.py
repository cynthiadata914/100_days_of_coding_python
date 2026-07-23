import turtle as t
import random

pookie = t.Turtle()
pookie.shape("turtle")
pookie.color("purple")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

pookie.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        pookie.color(random_color())
        pookie.circle(100)
        pookie.setheading(pookie.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

