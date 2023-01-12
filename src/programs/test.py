



class Ed:
	def __init__(self, x = None):
		if x:
			if isinstance(x, self.__class__): print(f'it is!! {type(x)}') 
			else: print(f"nah, it is {type(x)}")

x = Ed()
y = Ed(x)