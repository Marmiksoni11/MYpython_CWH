import turtle as t 


t.speed(100)
t.bgcolor("black")
colors = ["cyan"]
for i in range(240):
    t.color(colors[i%1])
    t.circle(i)
    t.left(5)
  


t.mainloop()