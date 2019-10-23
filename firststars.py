# This does a star with Juan & I.
import turtle
turtle.write("hello world", "center")

#turtle.shapetransform(25, 10, 15, 1)

turtle.color("red", "green")
turtle.colormode("blue")
turtle.speed(20)


for i in range(5):
    turtle.forward(200)
    turtle.right(144)
    turtle.clear()
    for i in range(5):
        turtle.fd(50)
        turtle.rt(144)
        for i in range(5):
            turtle.fd(10)
            turtle.rt(144)

turtle.done()
