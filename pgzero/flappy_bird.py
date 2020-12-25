import pgzrun


WIDTH = 500
HEIGHT = 500

hero = Actor('smallbird')
score = 0
speed = 3
game_over = False

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
    screen.blit("background", (0, 0))
    if game_over:
        screen.draw.text(f"Game Over", (5, 5), color="orange")
    else:
        hero.draw()
        screen.draw.text(f"score: {score}", (5, 5), color="orange")

        for i in aliens:
            i.draw()

def update():
    global speed, score, game_over


    # if hero.collidelist(aliens):
    #     print ('collided')
    #     return 
    for a in aliens:
        if hero.colliderect(a) == True:
            game_over = True
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