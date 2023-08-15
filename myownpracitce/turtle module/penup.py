import turtle as t 



s = t.Turtle()
t.bgcolor("black")
t.speed(100)
t.begin_fill()
t.color("orange","yellow")
t.pensize(1.5) #thicker pen

for i in range(100):
    for colors in ["yellow","green","red","white","cyan","blue"]:
        t.color(colors)
        t.fd(100)
        t.rt(90)
        t.fd(100)

        # t.penup()

        t.fd(100)
        t.rt(90)
        t.fd(100)

        # t.pendown()


        t.fd(100)
        t.rt(90)
        t.fd(100)

        # t.penup()

        t.fd(100)
        t.rt(90)
        t.fd(100)

        # t.pendown()

        t.right(25)

        t.fd(100)
        t.rt(90)
        t.fd(100)

        # t.penup()

        t.fd(100)
        t.rt(90)
        t.fd(100)

        # t.pendown()


        t.fd(100)
        t.rt(90)
        t.fd(100)

        # t.penup()

        t.fd(100)
        t.rt(90)
        t.fd(100)

    # t.pendown()
t.end_fill()
t.mainloop()