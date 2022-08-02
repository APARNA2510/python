import pgzrun
HEIGHT = 600
WIDTH = 600

player1 = Actor('alien', pos=(200,200))
player2 = Actor('alien', pos=(100,100))
enemy1 = Actor('enemy', pos=(400,400))
enemy2 = Actor('enemy', pos=(500,500))

#music.play('bg')

def draw():
    screen.clear()
    screen.blit('background', (0,0))
    player1.draw()
    player2.draw()
    enemy1.draw()
    enemy2.draw()

def enemy_chase_logic1():
    if enemy1.x > player1.x:
        enemy1.x -= 1
    if enemy1.x < player1.x:
        enemy1.x += 1
    if enemy1.y > player1.y:
        enemy1.y -= 1
    if enemy1.y < player1.y:
        enemy1.y += 1
    if enemy1.colliderect(player1):
        # sounds.splat.play()
        player1.image = 'splat'

def player1_control():
    if keyboard.left:
        player1.x -= 2
    if keyboard.right:
        player1.x += 2
    if keyboard.up:
        player1.y -= 2
    if keyboard.down:
        player1.y += 2

def player1_limit_check():
    if player1.x < 0:
        player1.x = WIDTH
    if player1.x > WIDTH:
        player1.x = 0
    if player1.y < 0:
        player1.y = HEIGHT
    if player1.y > HEIGHT:
        player1.y = 0

def enemy_chase_logic2():
    if enemy2.x > player2.x:
        enemy2.x -= 1
    if enemy2.x < player2.x:
        enemy2.x += 1
    if enemy2.y > player2.y:
        enemy2.y -= 1
    if enemy2.y < player2.y:
        enemy2.y += 1
    if enemy2.colliderect(player2):
        # sounds.splat.play()
        player2.image = 'splat'

def player2_control():
    if keyboard.left:
        player2.x -= 2
    if keyboard.right:
        player2.x += 2
    if keyboard.up:
        player2.y -= 2
    if keyboard.down:
        player2.y += 2

def player2_limit_check():
    if player2.x < 0:
        player1.x = WIDTH
    if player2.x > WIDTH:
        player2.x = 0
    if player2.y < 0:
        player2.y = HEIGHT
    if player2.y > HEIGHT:
        player2.y = 0        

def update():
    enemy_chase_logic1()
    player1_control()
    player1_limit_check()
    enemy_chase_logic2()
    player2_control()
    player2_limit_check()

pgzrun.go()