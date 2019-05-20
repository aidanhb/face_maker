import math
import re
import turtle

from name_metrics import *


class Head:

    def __init__(self, name):
        self.name = name
        self.color = (sporkiness(name),
                      (1 - funkiness(name)),
                      in_orderedness(name))
        self.width = 20
        self.length = 5 + longness(name) * 25
        self.outline = 0
        self.hairs = int(10 * sum_mod(name)) or 1
        self.hair_length = 10 + sporkiness(name) * 50 + funkiness(name) * 40
        self.hair_angle = 10 + 80 * sporkiness(name) + 90 * bounciness(name)
        self.hair_thickness = abs(30 * sporkiness(name) - 20 * sum_mod(name))
        self.hair_color = (1 - sporkiness(name),
                           min(in_orderedness(name) + 0.2, 1.0),
                           min(pyramidiness(name) + 0.1, 1.0))
        self.hair_straight = ((repeatiness(self.name) * 100) % 2) == 0
        sm = sum_mod(name)
        if sm < (1 / 3):
            self.shape = "circle"
        elif sm < (2 / 3):
            self.shape = "square"
        else:
            self.shape = "triangle"

    def draw_hair(self):
        shape_points = turtle.get_shapepoly()
        max_y = max(shape_points, key=lambda t: t[1])[1]
        all_max_x = [pt[0] for pt in shape_points if pt[1] == max_y]
        lft_x = min(all_max_x)
        rgt_x = max(all_max_x)
        hair_points = [(x, max_y) for x in linspace(lft_x, rgt_x, self.hairs)]
        headings = linspace(self.hair_angle, 2 * self.hair_angle, self.hairs)
        for i in range(self.hairs + 1):
            turtle.goto(hair_points[i])
            turtle.setheading(headings[i])
            turtle.pensize(self.hair_thickness)
            turtle.pencolor(self.hair_color)
            turtle.pendown()
            if self.hair_straight:
                rad_len = 180 * self.hair_length / (self.hair_angle * math.pi)
                radius = -rad_len if ends_with_vowel(self.name) else rad_len
                turtle.circle(radius, self.hair_angle)
            else:
                turtle.forward(self.hair_length)
            turtle.penup()
        turtle.pencolor("black")

    def draw(self):
        turtle.home()
        turtle.setheading(90)
        turtle.shape(self.shape)
        turtle.shapesize(self.length, self.width, self.outline)
        turtle.fillcolor(self.color)
        turtle.stamp()
        turtle.hideturtle()
        self.draw_hair()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        turtle.hideturtle()


class Eyes:

    def __init__(self, name):
        self.name = name
        self.separation = (15 + sporkiness(name) * 70 +
                           ends_with_vowel(name) * 20 +
                           percussiveness(name) * 30 +
                           funkiness(name) * 30 +
                           repeatiness(name) * 20 +
                           palindrominess(name) * 30)
        self.eye_level = 15 + sum_mod(name) * 100 + funkiness(name)
        self.width = 4 * funkiness(name) + 1
        self.eye_height = 4 * bounciness(name) + 1
        self.angle = 180 - (10 * sum_mod(name))
        self.eyebrow_angle = 5 - (10 * sporkiness(name))
        self.eyebrow_thickness = 30 * funkiness(name)
        self.eyebrow_length = 30 + 30 * repeatiness(name)
        self.outline = 6 * in_orderedness(name)
        self.offset = starts_with_vowel(self.name) * 5 - sporkiness(self.name)

    def draw_eye(self):
        turtle.shapesize(self.width, self.eye_height, self.outline)
        turtle.fillcolor("white")
        turtle.shape("circle")
        turtle.stamp()
        turtle.shapesize(1, 1, 1)
        turtle.fillcolor("black")
        turtle.stamp()

    def draw_eyebrow(self, side):
        right_x = side * (self.separation / 2 - self.eyebrow_length / 2)
        turtle.goto(right_x, self.eye_level + (self.eye_height * 10))
        turtle.setheading(90 - side * 90 + side * self.eyebrow_angle)
        turtle.pensize(self.eyebrow_thickness)
        turtle.pencolor("black")
        turtle.pendown()
        turtle.forward(self.eyebrow_length)
        turtle.penup()

    def draw(self):
        turtle.goto(self.separation / 2, self.eye_level)
        turtle.setheading(self.angle)
        self.draw_eye()
        self.draw_eyebrow(1)
        turtle.goto(-(self.separation / 2), self.eye_level + self.offset)
        turtle.setheading(180 - self.angle)
        self.draw_eye()
        self.draw_eyebrow(-1)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        turtle.hideturtle()


class Nose:

    def __init__(self, name):
        self.color = ((sporkiness(name) + 0.2) % 1,
                      (1 - funkiness(name)),
                      in_orderedness(name))
        self.length = 40 * longness(name) + 30 * palindrominess(name)
        self.width = 30 * sporkiness(name) + 20 * bounciness(name)

    def draw(self):
        turtle.fillcolor(self.color)
        turtle.goto(-self.width, self.length)
        turtle.setheading(270)
        turtle.pensize(5)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(self.length)
        turtle.circle(self.width, 180)
        turtle.forward(self.length)
        turtle.end_fill()
        turtle.penup()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        turtle.hideturtle()


class Mouth:

    def __init__(self, name):
        self.angle = 180 * sporkiness(name)
        self.radius = 100 * funkiness(name)
        self.position = 80 + 50 * repeatiness(name)
        self.tongue = thness(name)

    def draw(self):
        if self.tongue:
            turtle.fillcolor((1.0, 0.1, 0.2))
            turtle.goto(-10, -self.position)
            turtle.setheading(270)
            turtle.pensize(0)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(10, 180)
            turtle.end_fill()
            turtle.penup()
        turtle.goto(0, -self.position)
        turtle.setheading(0)
        turtle.pensize(5)
        turtle.pendown()
        turtle.circle(self.radius, self.angle / 2)
        turtle.penup()
        turtle.goto(0, -self.position)
        turtle.setheading(180)
        turtle.pendown()
        turtle.circle(-self.radius, self.angle / 2)
        turtle.penup()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        turtle.hideturtle()


def main():
    while True:
        name = input("What is your name? ").strip().lower()
        if not re.match("^[a-z ]+$", name):
            print("Name must only contain letters and spaces.")
        else:
            turtle.reset()
            with Head(name) as head:
                head.draw()
            with Mouth(name) as mouth:
                mouth.draw()
            with Nose(name) as nose:
                nose.draw()
            with Eyes(name) as eyes:
                eyes.draw()


if __name__ == "__main__":
    main()
