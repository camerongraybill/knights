from Move import Move

class Board:
	knight = 'k'
	empty = 'e'
	visited = 'v'
	
	def __init__(self, size, start=(0, 0)):
		self.__max = size
		self.__board_state = {}
		for x in range(self.__max):
			for y in range(self.__max):
				self.__board_state[(x, y)] = self.empty
		self.__board_state[start] = self.knight
	
	def get_knight_pos(self):
		for k, v in self.__board_state.iteritems():
			if v == self.knight:
				return k
	
	def apply_move(self, move):
		if not self.is_valid_move(move):
			raise Exception("Invalid move: " + str(move))
		(x, y) = self.get_knight_pos()
		self.__board_state[(x, y)] = self.visited
		new_pos = (x + move.x, y + move.y)
		self.__board_state[new_pos] = self.knight
	
	def is_valid_move(self, move):
		(x, y) = self.get_knight_pos()
		x += move.x
		y += move.y
		if not (0 <= x <= self.__max - 1 and 0 <= y <= self.__max - 1):
			return False
		return self.__board_state[(x, y)] != self.visited

	def get_valid_moves(self):
		return [Move(x[0], x[1]) for x in Move.possible_moves if self.is_valid_move(Move(x[0], x[1]))]
		
	def is_full(self):
		return all([v != self.empty for k, v in self.__board_state.iteritems()])
	
	def __getitem__(self, idx):
		return self.__board_state[idx]
	
	def __repr__(self):
		out = ""
		for i in range(self.__max):
			out += str(self[i, 0])
			for j in range(1, self.__max):
				out += " " + str(self[i, j])
			out += "\n"
		return out
