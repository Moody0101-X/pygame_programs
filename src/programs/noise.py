
import pygame
from BoilerPlate import code
from random import randint
from math import sin, tan, cos, sqrt
from numpy import random
from dataclasses import dataclass

class Point:
	def __init__(self, win, x, y, color, radius):
		self.win = win
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.color = color
		self.radius = radius

	def setdimensions(self, w, h):
		self.w = w
		self.h = h

	def draw(self):
		if self.x < self.w - 50 and self.y < self.h - 50:
			pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)


@dataclass
class vector2D:
	x: float = 0
	y: float = 0

	def __add__(self, other):
		if isinstance(other, self.__class__):
			self.x += other.x
			self.y += other.y
		# 	return
		# self.x += other
		# self.y += other

	def __sub__(self, other):
		if isinstance(other, self.__class__):
			self.x -= other.x
			self.y -= other.y
		# 	return
		# self.x -= other
		# self.y -= other

	def __mul__(self, other):
		if isinstance(other, self.__class__):
			return vector2D(self.x * other.x, self.y * other.y)
		return vector2D(self.x * other, self.y * other)

	def __div__(self, other):
		if isinstance(other, self.__class__):
			return vector2D(self.x / other.x, self.y / other.y)
		return vector2D(self.x / other, self.y / other)

	def __radd__(self, other):
		return self.__add__(other)

	def __rsub__(self, other):
		return self.__sub__(other)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __rdiv__(self, other):
		return self.__div__(other)
	
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.x == other.x and self.y == other.y
		return self.x == other and self.y == other
	def __repr__(self):
		return f"({self.x}, {self.y})"

def dot(vec1: vector2D, vec2: vector2D):
	""" if the return is:
	1: PARALLEL
	0: PERPENDICULAR
	-1: OPOSITE
	"""
	return vec1.x * vec2.x + vec1.y * vec2.y
@dataclass
class randomVec(vector2D):
	def __init__(self, *arg, **kwargs):
		super().__init__(*arg, **kwargs)
		self.x = randint(-20, 20)
		self.y = randint(-20, 20)

class boid:

	def __init__(self, win, width, height, color=(255, 255, 255)):
		self.win = win
		self.width = width
		self.height = height
		self.color = color
		self.position: vector2D = vector2D(self.width / 2, self.height / 2)
		self.velocity: randomVec = randomVec()

		self.acceleration:vector2D = vector2D(2, 1)

	def update(self):
		self.velocity: randomVec = randomVec()
		self.position.__add__(self.velocity)
		self.velocity.__add__(self.acceleration)

	def draw(self):

		pygame.draw.circle(self.win, self.color, (self.position.x, self.position.y), 1)

class Drawer(code):
	""" A cirlce wrapper class that inherits from code. """

	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.flock = [boid(self.window, self.width, self.height) for i in range(10000)]
		self.run_()


	def draw(self) -> None:
		for i in self.flock:
			i.draw()
		

	def run_(self) -> None:
		self.clock.tick(60)
		while self.run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
			pygame.display.update()
			self.window.fill(self.Backgroundcolor)
			for i in self.flock:
				i.update()
			self.draw()
		pygame.quit()

if __name__ == "__main__":
	Drawer("Noise", (0, 0, 0), 1080, 720)
