import pygame, math, sys

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")

# variables
rect1x = 900
rect1y = 50
rect2x = 600
rect2y = 420
rect1_mass = 150
rect2_mass = 400
G = 1.62

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))

    rect1 = pygame.Rect(rect1x,rect1y,30,30)
    rect2 = pygame.Rect(rect2x,rect2y,70,70)

    distance = round(math.sqrt((rect2x-rect1x)*(rect2x-rect1x)+(rect2y-rect1y)*(rect2y-rect1y)),5)
    F = round(G*((rect1_mass*rect2_mass)/(distance*distance)),5)

    rect1x -= F
    rect1y += G
    rect2x -= 0.6

    if (rect1y>=767):
        sys.exit()

    pygame.draw.rect(window, (255,255,255), rect1)
    pygame.draw.rect(window, (255,255,255), rect2)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
