import turtle

turtle.bgcolor("black")
turtle.pencolor("green")
turtle.speed(0)
turtle.penup()
turtle.setpos(0, 200)
turtle.pendown()
turtle.hideturtle()

a = 0

for b in range(210):
    turtle.forward(a)
    turtle.right(b)
    a += 3

turtle.done()
