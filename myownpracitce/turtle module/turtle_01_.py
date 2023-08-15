#creating a screen

import turtle as t
s = t.getscreen()
t.begin_fill()
t.screensize()
t.screensize(1920,1200)
t.screensize()
# t.bgcolor("yellow")
t.title("MYSCREEEN")
# for i in range(14):
#    t.right(25) # angle 25 degrees 
#    t.forward(50)


# t.ht() #hides arrow/turtle
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.shape("turtle")
# t.shape("arrow")
# t.shape("circle")
# t.shapesize(1,1,1) #turtle shape size changing
# t.fillcolor("blue")
t.color("yellow","red")
t.speed('fastest')
t.bgcolor("black")
# t.pensize(4) #thicker pen
#my first pattern 
for i in range(140):
    for colors in ["yellow","green","red","white","cyan","blue"]:
        t.color(colors)
        t.circle(60)
        t.dot(10)
        t.right(25)
        t.forward(100)
        t.fd(100)  
        t.lt(120)
        t.dot(10)
        t.right(25)
        t.speed(50)


t.end_fill()
t.mainloop()


