from __future__ import print_function
from Move import Move
from Board import Board
import random
import sys

def random_search_solver(b):
	cp = b.copy()
	path = []
	while not cp.is_full():
		cp = b.copy()
		moves = cp.get_valid_moves()
		visited_states = []
		path = [(0,0)]
		while moves:
			move = random.choice(moves)
			visited_states.append(str(cp))
			cp.apply_move(move)
			path.append(cp.get_knight_pos())
			moves = cp.get_valid_moves()
	return path
		

def dfs(b, d=0, visited=[]):
	if b.is_full():
		return []
	for option in b.get_valid_moves():
		cp = b.copy().apply_move(option)
		if str(cp) in visited:
			continue
		visited.append(str(cp))
		try:
			for _ in range(d):
				print("    ", end="")
			print(option)
			return [option].extend(dfs(cp, d+1, visited))
		except Exception:
			pass
	raise Exception()
		


start = (0,0)
	
try:
	b = Board(int(sys.argv[1]), start)
except Exception:
	b = Board(8, start)
	
print(dfs(b))