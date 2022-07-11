from turtle import *

speed('fastest')
bgcolor('black')
pencolor('white')
penup()
setpos(100,100)
pendown()
for i in range(100,0,-3):
    forward(i)
    left(90)

penup()
setpos(-100,100)
pendown()
for i in range(100,0,-3):
    forward(i)
    left(90)  

penup()
setpos(-100,-100)
pendown()
for i in range(100,0,-3):
    forward(i)
    left(90) 

penup()
setpos(100,-100)
pendown()
for i in range(100,0,-3):
    forward(i)
    left(90)   

mainloop()          