"""
this module helps you draw cirlces in pygame.
"""


import pygame
from random import choice, randint, uniform
from .BoilerPlate import code
from math import sin, tan, cos, sqrt
from numpy import random

class pixel:
    
    def __init__(self, win, x, y, color, radius):
        self.win = win
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.velocity = 4
        self.Ydirection = 1
        self.Xdirection = 1
  
    def setdimensions(self, w, h):
        self.w = w
        self.h = h

    def draw(self):
        if self.x < self.w - 50 and self.y < self.h - 50:
            pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)
            
    def move(self):
        
        if self.x >= self.w - 50:
            self.Xdirection = -1
        elif self.x <= 50:
            self.Xdirection = 1
        if self.y >= self.h - 50:
            self.Ydirection = -1
        elif self.y <= 50:
            self.Ydirection = 1
        
        self.y += self.Ydirection * randint(0, 5) * uniform(0, 1) * randint(0, 5) * choice([-1, 1])
        self.x +=  self.Xdirection * randint(0, 5) * uniform(0, 1) * randint(0, 5) * choice([-1, 1])

class ArtGenerator(code):
    """ A cirlce wrapper class that inherits from code. """

    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)
        self.circles = [
            pixel(self.window, x, y, (0, 0, randint(0, 50)), 10) for x, y in zip([ i for i in range(50, 300)], [ i for i in range(50, 300)])
        ]

        self.run_()

    def draw(self) -> None:
        for i in self.circles:
            i.draw()

    def run_(self) -> None:
        self.clock.tick(30)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            pygame.display.update()
            # self.window.fill(self.Backgroundcolor)
            for i in self.circles:
                i.setdimensions(self.width, self.height)
                i.move()
                # i.drawCircle()
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    ArtGenerator("Circle", (255, 255, 255), 1080, 720)

"""

RGBA ALPHA
(R, G, B) => RED, GREEN, BLUE
(0, 0, 0) => black
(255, 255, 255) => white
(0, 0, 100) => purple
(?, 0, ?) => pink

"""