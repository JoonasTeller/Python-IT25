#Joonas Teller
#10.11.25




import turtle
t = turtle.Turtle()
aken = turtle.Screen()
aken.setup(width=500, height=400)
aken.title("Olümpiarõngad - Joonas")

t.speed(0)
#Sinine
t.penup()
t.goto(-110,0)
t.pendown()
t.pensize(6)
t.pencolor("blue")

t.circle(50)
#Must
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(6)
t.pencolor("black")

t.circle(50)
#Punane
t.penup()
t.goto(110,0)
t.pendown()
t.pensize(6)
t.pencolor("red")

t.circle(50)
#Kollane
t.penup()
t.goto(-55,-55)
t.pendown()
t.pensize(6)
t.pencolor("yellow")

t.circle(50)
#Roheline
t.penup()
t.goto(55,-55)
t.pendown()
t.pensize(6)
t.pencolor("green")

t.circle(50)


turtle.done()