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

	def get_index_worst_piece(self):
		indeks = -1
		diff = 999
		for i in range(len(self.list)):
			piece = self.list[i]
			selisih = self.get_attacked_difference(piece)
			if selisih < diff:
				diff = selisih
				indeks = i
		return indeks

	def move_one_piece(self, selisih_board, temperature):
		indeks = self.get_index_worst_piece()
		piece = self.list[indeks]
		saved_x = piece.x
		saved_y = piece.y
		selisih = self.get_attacked_difference(piece)
		point = self.get_random_location()
		piece.x = point['x']
		piece.y = point['y']
		new_selisih = self.get_attacked_difference(piece)
		atk = self.summary_attacked()
		new_selisih_board = atk['opponent'] - atk['teamates']
		if (new_selisih < selisih or new_selisih_board < selisih_board) and temperature != 0:
			probability = math.exp(new_selisih / temperature)
			p = random.random()
			if p > probability:
				point = self.get_random_location()
				piece.x = point['x']
				piece.y = point['y']
			else:
				piece.x = saved_x
				piece.y = saved_y






