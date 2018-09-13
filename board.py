import random

class Board:
	def __init__(self):
		self.list = []

	def print_board(self):
		map = self.init_map()

		for li in self.list:
			map[li.x - 1][li.y - 1] = li.serialize

		for row in map:
			for column in row:
				print(column, end=' ')
			print()


	def init_map(self):
		map = []
		for i in range(8):
			map.append(['.','.','.','.','.','.','.','.'])
		return map

	def add_piece(self, piece):
		self.list.append(piece)

	def get_random_location(self):
		already_taken = True
		point = {}
		while already_taken:
			point['x'] = random.randint(1, 9)
			point['y'] = random.randint(1, 9)
			already_taken = self.is_taken(point['x'], point['y'])
		return point

	def is_taken(self, x, y):
		for li in self.list:
			if li.x == x and li.y == y:
				return True
		return False
