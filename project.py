import turtle

daniil = turtle.Turtle()
turtle.bgcolor("black")
daniil.speed(0)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

for i in range(100):
    daniil.color(colors[i % len(colors)])
    daniil.forward(i * 4)
    daniil.right(91)



daniil.hideturtle()
turtle.done()

