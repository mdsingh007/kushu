''' 
1 - move aliens
    a) move aliens horizontally; aliens should oscillate horizontally 
    b) move aliens vertical


'''




import pgzrun

WIDTH = 1200
HEIGHT  = 700

hero = Actor('shooter')
aliens_in_row = 11
rows_of_aliens = 5

hgap = 80
top_left_alien_x = (WIDTH / 2) - (hgap*5) - 100
ypos = 50
alien_move_x = 0
alien_move_y = 0

aliens = []
for y in range(rows_of_aliens):
    alienrow = []
    for i in range(aliens_in_row):
        a = Actor('s')
        a.visible = True
        alienrow.append( a )
        a.pos = top_left_alien_x + (hgap*i), ypos*(y+2)
    aliens.append(alienrow)

hero.pos= WIDTH/2, HEIGHT - hero.height

def move_alien():
    global alien_move_x
    if aliens[0][0].x + 11*hgap > WIDTH:
        alien_move_x -= 20
    else:
        alien_move_x  += 20


clock.schedule_interval(move_alien, 1.0)

def draw():
    screen.fill((0, 0, 0))
    box_color = 255, 255, 255
    BOX = Rect((0, 0), (WIDTH, 40))
    screen.draw.rect(BOX, box_color)
    screen.draw.text("score: ", (10, 20))
    screen.draw.text("lives: ", (WIDTH - 100, 20))
    for i in aliens:
        for a in i:
            a.draw()
    hero.draw()

def update():
    global top_left_alien_x, hgap        

    for y, arow in enumerate(aliens):
        for i, a in enumerate(arow):
            a.pos = top_left_alien_x + (hgap*i) + alien_move_x, ypos*(y+2)

        # for a in aliens:
        #     a.x = a.x + alien_move_x
    
    print(alien_move_x)

        # Ensure hero does not go out of screen
    if hero.x > WIDTH - 35:
        hero.x = WIDTH - 35
    if hero.x < HEIGHT - HEIGHT + 35:
        hero.x = HEIGHT - HEIGHT + 35
    
    # move hero up/down
    if keyboard[keys.RIGHT]:
        hero.x += 3
    if keyboard[keys.LEFT]:
        hero.x -= 3





pgzrun.go()