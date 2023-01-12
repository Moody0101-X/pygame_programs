"""
Drawing shapes using python and shape equations:

circle:
	x^2 + y^2 = r^2
	x = sqrt(r^2 - y^2)
	y = sqrt(r^2 - x^2)

"""


import pygame
from BoilerPlate import code
from random import randint
from math import sin, tan, cos, sqrt
from numpy import random


class Point:
	def __init__(self, win, x, y, color, radius):
		self.win = win
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.color = color
		self.radius = radius
		self.r = 200
		self.velocity = 4
		self.Ydirection = 1
		self.Xdirection = 1
		self.ang = 0

	def setdimensions(self, w, h):
		self.w = w
		self.h = h

	def draw(self):
		if self.x < self.w - 50 and self.y < self.h - 50:
			pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)

	def drawCircle(self):
		""" draws a circle. """

		if self.ang % 360 == 0:
			self.color = (randint(200, 255), randint(200, 255), randint(200, 255))
			if self.ang > 360 * 2:
				self.r += 10
			if self.ang > 360 * 4:
				self.r -= 10
		self.x += self.r * sin(self.ang)
		self.y += self.r * cos(self.ang)

	def drawRect(self):
		""" draws a rectangle, signiture for now """
		pass


class Drawer(code):
	""" A cirlce wrapper class that inherits from code. """

	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.point = Point(self.window, self.width/2 - 180, self.height/2 - 100, (255, 255, 255), 1)
		self.point2 = Point(self.window, self.width/2 - 100 * 2, self.height/2 - 100, (255, 255, 255), 1)
		self.point3 = Point(self.window, self.width/2 - 100 * 2.2, self.height/2 - 100, (255, 255, 255), 1)
		self.point4 = Point(self.window, self.width/2 - 100 * 2.4, self.height/2 - 100, (255, 255, 255), 1)
		self.point5 = Point(self.window, self.width/2 - 100 * 2.8, self.height/2 - 100, (255, 255, 255), 1)
		self.origin = Point(self.window, self.width/2, self.height/2, (19, 19, 19), 10)
		self.run_()


	def draw(self) -> None:
		self.point.draw()
		self.point2.draw()
		self.point3.draw()
		self.point4.draw()
		self.point5.draw()
		self.origin.setdimensions(self.width, self.height)
		self.origin.draw()
		self.point.ang += 1
		self.point2.ang += 1
		self.point3.ang += 1
		self.point4.ang += 1
		self.point5.ang += 1


	def run_(self) -> None:
		self.clock.tick(60)
		while self.run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
			pygame.display.update()
			# self.window.fill(self.Backgroundcolor)            
			self.point.setdimensions(self.width, self.height)
			self.point2.setdimensions(self.width, self.height)
			self.point3.setdimensions(self.width, self.height)
			self.point4.setdimensions(self.width, self.height)
			self.point5.setdimensions(self.width, self.height)
			self.point.drawCircle()
			self.point2.drawCircle()
			self.point3.drawCircle()
			self.point4.drawCircle()
			self.point5.drawCircle()

			self.draw()
		pygame.quit()

if __name__ == "__main__":
	Drawer("Circle", (255, 255, 255), 1080, 720)
