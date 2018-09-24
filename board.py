import random
import math

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

	def print_info(self):
		for piece in self.list:
			attack = piece.count_piece_atacked(self)
			if piece.team == 'WHITE':
				team = 'WHITE'
				enemies = 'BLACK'
			else:
				team = 'BLACK'
				enemies = 'WHITE'
			print(piece.serialize + " " + piece.team + " can attack " + str(attack[enemies]) + " enemies. and " + str(attack[team]) + " teamates")

	def init_map(self):
		map = []
		for i in range(8):
			map.append(['.','.','.','.','.','.','.','.'])
		return map

	def print_piece(self):
		for li in self.list:
			li.print_location()

	def add_piece(self, piece):
		self.list.append(piece)

	def get_random_location(self):
		already_taken = True
		point = {}
		while already_taken:
			point['x'] = random.randint(1, 8)
			point['y'] = random.randint(1, 8)
			already_taken = self.is_taken(point['x'], point['y'])
		return point

	def is_taken(self, x, y):
		for li in self.list:
			if li.x == x and li.y == y:
				return True
		return False

	def summary_attacked(self):
		teamates = 0
		opponent = 0
		for piece in self.list:
			atk = piece.count_piece_atacked(self)
			teamates = teamates + atk[piece.team]
			opponent = opponent + atk[piece.get_opponent()]
		return {'teamates': teamates, 'opponent': opponent}


	def get_attacked_difference(self, piece):
		teamates = 0
		opponent = 0
		atk = piece.count_piece_atacked(self)
		teamates = teamates + atk[piece.team]
		opponent = opponent + atk[piece.get_opponent()]
		selisih = opponent - teamates
		return selisih






