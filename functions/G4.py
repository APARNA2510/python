import pgzrun

HEIGHT = 500
WIDTH = 500

p = Rect((40,40),(50,50))

def draw():
    screen.fill('white')
    screen.draw.filled_rect(p,'blue')

def update():
    control_player()
    check_boundary1()

def control_player():
    if keyboard.RIGHT:
        if p.right < WIDTH:
            p.x += 2
        else:
            sounds.hit.play()    
    if keyboard.LEFT:
        if p.left > 0:
            p.x += -2
        else:
            sounds.hit.play()    
    if keyboard.UP:
        p.y += -2
    if keyboard.DOWN:
        p.y += 2 

def check_boundary1(): 
    if p.x > WIDTH:
        p.x = 0
    if p.x < 0:
        p.x = WIDTH
    if p.y > HEIGHT:
        p.y = 0
    if p.y < 0:
        p.y = HEIGHT        

pgzrun.go()     