from turtle import *

colors = ['red','blue','green','yellow','purple','orange']

for i in range(100):
    s = len(colors)
    c = colors[i%s]
    pencolor(c)
    forward(i+5)
    left(60) #left(360/s)

mainloop()    