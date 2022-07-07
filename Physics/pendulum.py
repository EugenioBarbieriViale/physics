# Sources:
# https://www.myphysicslab.com/pendulum/pendulum-en.html
# https://www.youtube.com/watch?v=NBWMtlbbOag
# http://calculuslab.deltacollege.edu/ODE/7-A-2/7-A-2-h.html

import pygame, sys
from numpy import sqrt, cos, arcsin, pi, sin

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

screen = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Pendulum")

length = 300
angle = 0.7 # radians
angleV = 0 # angular velocity
angleA = 0 # angular acceleration
gravity = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    x = length*sin(angle)+500
    y = length*cos(angle)+50
    force = sin(angle)*gravity

    angleA = (force*-1)/length
    angleV += angleA
    angle += angleV

    pygame.draw.line(screen, (255,255,255),(500,50), (x,y), width=3)
    pygame.draw.circle(screen, (0,0,255), (x,y), 30)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
