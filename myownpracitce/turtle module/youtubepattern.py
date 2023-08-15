import turtle as t

t.bgcolor("black")
t.speed(30)
colors = ["yellow","green","red","white","cyan","blue"]
for i in range(100):
        t.color(colors[i%6])
        t.fd(i*5)
        t.left(200)
        t.width(0)

t.mainloop()