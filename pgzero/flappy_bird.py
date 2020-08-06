import pgzrun

alien = Actor('alien')
alien2 = Actor('alien')
alien3 = Actor('alien')
alien4 = Actor('alien')
alien.pos = 250, 50
alien2.pos = 550, 5
alien3.pos = 550, 495 
alien4.pos = 550, 5

WIDTH = 500
HEIGHT = 500

def draw():
    # screen.clear()
    screen.fill((102, 230, 255))
    alien.draw()
    alien2.draw()
    alien3.draw()
    alien4.draw()

def update():
    if alien.colliderect(alien2) == True:
        print("collided")
        return
    if alien.colliderect(alien3) == True:
        print("collided")
        return
    if alien.colliderect(alien4) == True:
        print("collided")
        return

    if alien.y > 495:
        alien.y = 495
    if alien.y < 5:
        alien.y = 5
    if keyboard[keys.SPACE]:
        alien.y -= 3
    else:
        alien.y += 3

    alien2.x -= 3

    if alien2.x < 60:
        alien3.x -= 3

    if alien3.x < 60:
        alien4.x -= 3



pgzrun.go()