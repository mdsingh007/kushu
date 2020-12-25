'''
Coding excercise - 18 Dec 2020
 - Add splash screen
 - improve Game screen. e.g. Game over text should be in in center ofscreen. Show high score.
 - Game should restart after pressing space.
'''
import pgzrun


WIDTH = 500
HEIGHT = 500

hero = Actor('smallbird')
score = 0
speed = 3
game_state = 0 # 0 is splash screen; 1 is game ; 2 is game over
# game_over = False
# showsplash = True

def resume():
    global game_state
    game_state = 1
    set_original()
    return 


aliens = []
for i in range(3):
    a = Actor('alien')
    a.visible = True
    aliens.append( a )


def set_original():
    aliens[0].pos = 500, 50
    aliens[1].pos = 750, 250
    aliens[2].pos = 1000, 450

    for a in aliens:
        a.visible = True

set_original()
    


def draw():
    # screen.clear()
    screen.fill((102, 230, 255))
    if game_state == 0:
        screen.draw.text(f"Welcome to space invaders, press B to begin", (50, 220), color="blue", fontsize=30)
    elif game_state == 2:
        screen.draw.text(f"Game Over", (160, 220), color="orange", fontsize=50)
        screen.draw.text(f"press R to respawn", (100, 250), color="orange", fontsize=50)
    else:
        hero.draw()
        screen.draw.text(f"score: {score}", (5, 5), color="orange")

        for i in aliens:
            i.draw()

def update():
    global speed, score, game_state

    if game_state == 0:
        if keyboard[keys.B]:
            game_state = 1
        return

    if hero.collidelist(aliens) != -1: # -1 means no collision
        game_state = 2
        if keyboard[keys.R]:
            resume()
        return


    # Ensure hero does not go out of screen
    if hero.y > 495:
        hero.y = 495
    if hero.y < 5:
        hero.y = 5
    
    # move hero up/down
    if keyboard[keys.SPACE]:
        hero.y -= 3
    else:
        hero.y += 3

    for a in aliens:
        a.x -= speed


    for a in aliens:
        if a.visible and a.x < 0:
            score += 1
            a.visible = False

    if aliens[2].x < 0:
        set_original()
        speed += 1







pgzrun.go()

# Hero -> Bird
# Enemy should continiously come
# Play sound when collide
# Show score how many birds passed.