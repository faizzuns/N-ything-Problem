class Chess:
	MIN_INT = 1
	MAX_INT = 8

	def __init__(self, x, y, team):
		self.x = self.validate_location(x)
		self.y = self.validate_location(y)
		self.team = team

	def validate_location(self, position):
		if position >= self.MIN_INT and position <= self.MAX_INT:
			return position
		else:
			return self.MIN_INT

	def print_location(self):
		print("Location in (" + str(self.x) + "," + str(self.y) + ")")

	def horizontal_vertical_piece_attacked(self, board):
		count = {'WHITE':0 , 'BLACK':0}
		left_attacked = False
		right_attacked = False
		bottom_attacked = False
		top_attacked = False
		for piece in board.list:
			if self.x == piece.x:
				if piece.y < self.y and not left_attacked:
					count[piece.team] = count[piece.team] + 1
					left_attacked = True
				elif piece.y > self.y and not right_attacked:
					count[piece.team] = count[piece.team] + 1
					right_attacked = True
			elif self.y == piece.y:
				if piece.x < self.x and not top_attacked:
					count[piece.team] = count[piece.team] + 1
					top_attacked = True
				elif piece.x > self.x and not bottom_attacked:
					count[piece.team] = count[piece.team] + 1
					bottom_attacked = True
		return count

	def diagonal_piece_attacked(self, board):
		count = {'WHITE':0 , 'BLACK':0}
		top_left_attacked = False
		top_right_attacked = False
		bot_left_attacked = False
		bot_right_attacked = False
		for piece in board.list:
			gradient = (self.y - piece.y) / (self.x - piece.x) if self.x != piece.x else 0
			if gradient == 1:
				if piece.y < self.y and not top_left_attacked:
					count[piece.team] = count[piece.team] + 1
					top_left_attacked = True
				elif piece.y > self.y and not bot_right_attacked:
					count[piece.team] = count[piece.team] + 1
					bot_right_attacked = True
			elif gradient == -1:
				if piece.x < self.x and not bot_left_attacked:
					count[piece.team] = count[piece.team] + 1
					bot_left_attacked = True
				elif piece.x > self.x and not top_right_attacked:
					count[piece.team] = count[piece.team] + 1
					top_right_attacked = True
		return count

	def l_piece_attacked(self, board):
		count = {'WHITE':0 , 'BLACK':0}
		for piece in board.list:
			gradient = (self.y - piece.y) / (self.x - piece.x) if self.x != piece.x else 0
			if gradient != -1 and gradient != 1 and gradient != 0:
				if piece.x > self.x - 3 and piece.x < self.x + 3:
					if piece.y > self.y - 3 and piece.y < self.y + 3:
						count[piece.team] = count[piece.team] + 1
		return count

	def get_opponent(self):
		if self.team == 'WHITE':
			return 'BLACK'
		else:
			return 'WHITE'

	def move_piece(self,x,y):
		self.x = x
		self.y = y

	def get_max_trial_value(self,board):
		max_x =0
		max_y =0
		max_eval = board.total_evaluation()
		saved_x = self.x
		saved_y = self.y
		for x in range (1,9):
			for y in range (1,9):
	 			if not board.is_taken(x,y):
	 				self.move_piece(x,y)
	 				if board.total_evaluation() > max_eval:
	 					max_x = x
	 					max_y = y
	 					max_eval = board.total_evaluation()
		self.move_piece(saved_x,saved_y)
		if max_x == 0 and max_y == 0:
			max_x = saved_x
			max_y = saved_y
		return {'max_x': max_x,
				'max_y': max_y, 
				'max_eval': max_eval}

class Queen(Chess):
	def __init__(self, x, y, team):
		super().__init__(x, y, team)
		if team == 'WHITE':
			self.serialize = 'Q'
		else:
			self.serialize = 'q'

	def print_location(self):
		print(self.team + " Queen Location in (" + str(self.x) + "," + str(self.y) + ")")

	def count_piece_attacked(self, board):
		attack_diagonal = self.diagonal_piece_attacked(board)
		attack_hor_ver = self.horizontal_vertical_piece_attacked(board)
		attack_black = attack_diagonal['BLACK'] + attack_hor_ver['BLACK']
		attack_white = attack_diagonal['WHITE'] + attack_hor_ver['WHITE']
		attack = {
			'BLACK' : attack_black,
			'WHITE' : attack_white}
		return attack

class Knight(Chess):
	def __init__(self, x, y, team):
		super().__init__(x, y, team)
		if team == 'WHITE':
			self.serialize = 'K'
		else:
			self.serialize = 'k'

	def print_location(self):
		print(self.team + " Knight Location in (" + str(self.x) + "," + str(self.y) + ")")

	def count_piece_attacked(self, board):
		return self.l_piece_attacked(board)

class Bishop(Chess):
	def __init__(self, x, y, team):
		super().__init__(x, y, team)
		if team == 'WHITE':
			self.serialize = 'B'
		else:
			self.serialize = 'b'

	def print_location(self):
		print(self.team + " Bishop Location in (" + str(self.x) + "," + str(self.y) + ")")

	def count_piece_attacked(self, board):
		return self.diagonal_piece_attacked(board)

class Rook(Chess):
	def __init__(self, x, y, team):
		super().__init__(x, y, team)
		if team == 'WHITE':
			self.serialize = 'R'
		else:
			self.serialize = 'r'

	def print_location(self):
		print(self.team + " Rook Location in (" + str(self.x) + "," + str(self.y) + ")")

	def count_piece_attacked(self, board):
		return self.horizontal_vertical_piece_attacked(board) 


