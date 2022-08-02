import pgzrun

HEIGHT = 500
WIDTH = 500

box = Rect(50,50,100,100)
box2 = Rect(250,50,100,50)
box3 = Rect((400,400), (50,50))

def draw():
    screen.fill('black')
    screen.draw.rect(box,'red')
    screen.draw.filled_rect(box2,'white')
    screen.draw.filled_rect(box3,'yellow')
    screen.draw.text('These are Rectangles',(150,250),color='green')

pgzrun.go()    