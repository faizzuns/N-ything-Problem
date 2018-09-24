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
			print(piece.serialize + " " + piece.team + " can attack " + str(attack[enemies]) + " enemies. and " + str(attack[team]) + " teammates")

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

	def total_attack(self):
		teammates = 0
		opponents = 0
		for piece in self.list:
			attacked = piece.count_piece_atacked(self)
			teammates = teammates + attacked[piece.team]
			opponents = opponents + attacked[piece.get_opponent()]
		return {'teammates' : teammates, 'opponents' : opponents}

	def total_evaluation(self):
		lawan= self.total_attack()['opponents']
		kawan= self.total_attack()['teammates']
		return (lawan-kawan)

	def get_attacked_difference(self, piece):
		teammates = 0
		opponents = 0
		atk = piece.count_piece_atacked(self)
		teammates = teammates + atk[piece.team]
		opponents = opponents + atk[piece.get_opponent()]
		return (opponents-teammates)

#	def get_list_max_val(self):
#		trial = []
#		for piece in self.list:
#			max_val= self.get_difference(piece)
#			result = piece.get_max_trial_value(max_val, self)
#			trial.append(result['max_x'],result['max_y'],result['max_val'])
#	return (trial)

	def get_optimum_movement(self,listoflist):
		max_eval = -999
		for member in listoflist:
			if member[2]>max_eval:
				max_eval = member[2]
				m_x = member[0]
				m_y = member[1]
				piece = member[3]
		return {'max_x':m_x, 'max_y':m_y, 'max_eval':max_eval,'piece':piece}

	def is_taken(self, x, y):
		for li in self.list:
			if li.x == x and li.y == y:
				return True
		return False






