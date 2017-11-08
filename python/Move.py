class Move:
	possible_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
	
	def __init__(self, x, y):
		if (x,y) not in self.possible_moves:
			raise Exception("Invalid move: " + str((x,y)))
		self.x = x
		self.y = y
	
	def __getitem__(self, index):
		print str(index)
		return (self.x,self.y)[index]

	def __str__(self):
		return self.__repr__()
		
	def __repr__(self):
		return str((self.x, self.y))
