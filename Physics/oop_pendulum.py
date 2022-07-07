from numpy import sqrt, cos, arcsin, pi, sin

class Pendulum:
    def __init__(self, length, angle, gravity):
        self.length = length
        self.angle = angle
        self.gravity = gravity
        self.angleV = 0
        self.angleA = 0

    def move(self):
        self.x = self.length*sin(self.angle)+500
        self.y = self.length*cos(self.angle)+50
        self.angleA = -(sin(self.angle)*self.gravity)/self.length
        self.angleV += self.angleA
        self.angle += self.angleV
