import pygame, sys
from numpy import cos, pi, sin

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

screen = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Double Pendulum")

class doublePendulum():
    def __init__(self, angle1, angle2, mass1, mass2, length1, length2):
        self.angle1 = angle1
        self.angle2 = angle2

        self.length1 = length1
        self.length2 = length2

        self.mass1 = mass1
        self.mass2 = mass2

        self.angleA1 = 0
        self.angleA2 = 0
        self.angleV1 = 0
        self.angleV2 = 0
        self.forces = [0,0]

        self.x1 = 0
        self.y1 = 0

        self.x2 = 0
        self.y2 = 0
        self.px2 = -1
        self.py2 = -1

        self.gravity = 1
        self.endPoints = []

    def calc_angleA(self):
        exp1 = -self.gravity * (2 * self.mass1 + self.mass2) * sin(self.angle1)
        exp2 = self.mass2 * self.gravity * sin(self.angle1 - 2 * self.angle2)
        exp3 = 2 * sin(self.angle1 - self.angle2) * self.mass2 * ((self.angleV2 * self.angleV2) * self.length2 + (self.angleV1 * self.angleV1) * self.length1 * cos(self.angle1 - self.angle2))
        exp4 = self.length1 * (2 * self.mass1 + self.mass2 - self.mass2 * cos(2 * self.angle1 - 2 * self.angle2))
        self.forces[0] = (exp1 - exp2 - exp3) / (exp4)

        exp1 = 2 * sin(self.angle1 - self.angle2)
        exp2 = (self.angleV1 * self.angleV1) * self.length1 * (self.mass1 + self.mass2)
        exp3 = self.gravity * (self.mass1 + self.mass2) * cos(self.angle1)
        exp4 = (self.angleV2 * self.angleV2) * self.length2 * self.mass2 * cos(self.angle1 - self.angle2)
        exp5 = self.length2 * (2 * self.mass1 + self.mass2 - self.mass2 * cos(2 * self.angle1 - 2 * self.angle2))
        self.forces[1] = (exp1 * (exp2 + exp3 + exp4)) / (exp5)

    def move(self):
        self.x1 = self.length1*sin(self.angle1)+500
        self.y1 = self.length1*cos(self.angle1)+100
        self.x2 = self.length2*sin(self.angle2)+self.x1
        self.y2 = self.length2*cos(self.angle2)+self.y1

        self.endPoints.append((self.x2,self.y2))

        self.angleA1 = self.forces[0]
        self.angleA2 = self.forces[1]

        self.angleV1 += self.angleA1
        self.angleV2 += self.angleA2

        self.angle1 += self.angleV1
        self.angle2 += self.angleV2

    def draw(self):
        pygame.draw.line(screen, (255,255,255),(500,100), (self.x1,self.y1), width=3)
        pygame.draw.circle(screen, (255,0,0), (self.x1,self.y1), 30)
        pygame.draw.line(screen, (255,255,255),(self.x1,self.y1), (self.x2,self.y2), width=3)
        pygame.draw.circle(screen, (0,0,255), (self.x2,self.y2), 30)

    def track_path(self):
        for i in range(len(self.endPoints) - 1):
            pygame.draw.line(screen, (255, 255, 255), (int(self.endPoints[i][0]), int(self.endPoints[i][1])), (int(self.endPoints[i + 1][0]), int(self.endPoints[i + 1][1])), 2)

    def run(self):
        self.calc_angleA()
        self.move()
        self.track_path()
        self.draw()

ob = doublePendulum(1.5,0,10,10,200,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    ob.run()

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
