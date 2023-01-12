


import pygame
from dataclasses import dataclass
from math import sin, cos, tan, sqrt


class code:
    """Just an initializer, But running the Instance is manual."""
    def __init__(self, Title, Backgroundcolor=(255, 255, 255), width=None, height=None):
        self.Title = Title
        self.width = width
        self.height = height
        if not self.height:
            self.height = 500
        if not self.width:
            self.width = 500
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(self.Title)
        self.Backgroundcolor = Backgroundcolor
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(self.Backgroundcolor)
        self.run = True

@dataclass
class vector2D:
	""" Vector class to move objects.
		PROPS: x, y.

		`Pseoducode`

			DIRSTACK = [
				"Moveup",
				"Movedown",
				"Moveleft",
				"Moveright",
				"DiagonalupLeft",
				"Diagonalupright",
				"DiagonalbottomLeft",
				"Diagonalbottomright"
			]

			Methodology:

				Moveup: (x, y--)
				Movedown: (x, y++)
				Moveleft: (x--, y)
				Moveright: (x++, y)
				DiagonalupLeft: (x--, y--)
				Diagonalupright: (x++, y--)
				DiagonalbottomLeft: (x--, y++)
				Diagonalbottomright: (x++, y++)
			
			MoreMethodology:
				( If x == y ) {
					there would be an assymetric.
				}

				(If (x is random) && (y is random)) {
					The direction would not be included in the dir stack
				}

		Note: CLASS TYPE: GRAPHICS UTIL.
	"""

	x: int = 0
	y: int = 0

	def __add__(self, other):

		if isinstance(vector, self.__class__):
			self.x += other.x
			self.y += other.y
			return

		if isinstance(vector, int): 
			self.x += other
			self.y += other
			return

		if isinstance(other, tuple):
			self.x += other[0]
			self.y += other[1]
			return

		raise Exception(f"Other should be of type vector or int!! not {type(other)}")
	def __sub__(self, other):
		
		if isinstance(vector, self.__class__):
			self.x -= other.x
			self.y -= other.y
			return

		if isinstance(vector, int): 
			self.x -= other
			self.y -= other
			return

		if isinstance(other, tuple):
			self.x -= other[0]
			self.y -= other[1]
			return

		raise Exception(f"Other should be of type vector or int!! not {type(other)}")

	def __div__(self, other):
		if isinstance(vector, self.__class__):
			self.x /= other.x
			self.y /= other.y
			return
		if isinstance(vector, int): 
			self.x /= other
			self.y /= other
			return

		if isinstance(other, tuple):
			self.x /= other[0]
			self.y /= other[1]
			return

		raise Exception(f"Other should be of type vector or int!! not {type(other)}")

	def __mul__(self, other):
		if isinstance(other, self.__class__):
			self.x *= other.x
			self.y *= other.y
			return
		if isinstance(other, int): 
			self.x *= other
			self.y *= other
			return
		if isinstance(other, tuple):
			self.x *= other[0]
			self.y *= other[1]
			return

		raise Exception(f"Other should be of type vector or int!! not {type(other)}")

	def orbit(self, Pos, distance: int = 10):
		if Pos.x:
			if Pos.y:
				self.x = Pos.x + distance
				self.y = Pos.y + distance

		X, Y = distance * sin(self.ang), distance * cos(self.ang)

		self.__add__((X, Y))

class randomVec(vector2D):
	def __init__(self, *arg, **kwargs):
		super().__init__(*arg, **kwargs)
		self.x = randint(-20, 20)
		self.y = randint(-20, 20)



class moon:
	def __init__(self):
		self.vel = vector();


class planet:
	def __init__(self):

class ObjSimulationWin(code):
    """ A cirlce wrapper class that inherits from code. """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

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
                func = choice([i.move, i.move_, i.move__])
                func()
                # i.drawCircle()
            self.draw()
        pygame.quit()


def main(): #{
	ObjSimulationWin()
#}