#Joonas Teller
#10.11.25

import turtle

t = turtle.Turtle()
aken = turtle.Screen()
aken.setup(width=500, height=500)
aken.title("sinilill - Joonas")

t.speed(0)
t.pensize(10)
#Vars
t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor("green")
t.lt(90)
t.fd(200)

#Kroonlehed
t.pencolor("blue")
t.rt(90)
t.circle(80)

turtle.done()