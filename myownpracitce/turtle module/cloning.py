import turtle as t 

c = t.clone()
t.color("red")
c.color("blue")
t.speed(30)
t.circle(20)
c.circle(30)
for i in range(40,100,10):
    c.circle(i)

t.mainloop()
