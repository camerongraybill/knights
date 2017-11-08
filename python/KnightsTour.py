from Move import Move
from Board import Board
import random
import sys


try:
	b = Board(int(sys.argv[1]))
except Exception:
	b = Board(8)

start = (0,0)

moves = b.get_valid_moves()
visited_states = []
path = [start]
while moves:
	move = random.choice(moves)
	visited_states.append(str(b))
	b.apply_move(move)
	path.append(b.get_knight_pos())
	moves = b.get_valid_moves()
print path
print b