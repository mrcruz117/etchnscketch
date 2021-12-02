from turtle import Turtle, Screen

yurtle = Turtle()
screen = Screen()


def move_forward():
    yurtle.forward(15)


def move_back():
    yurtle.back(15)


def turn_left():
    new_heading = yurtle.heading() + 15
    yurtle.setheading(new_heading)


def turn_right():
    new_heading = yurtle.heading() - 15
    yurtle.setheading(new_heading)


def clear():
    yurtle.clear()
    yurtle.penup()
    yurtle.home()
    yurtle.pendown()


screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_back, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()
