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
		list_attacked = []
		return list_attacked

	def diagonal_piece_attacked(self, board):
		list_attacked = []
		return list_attacked

	def l_piece_attacked(self, board):
		list_attacked = []
		return list_attacked

class Queen(Chess):
	def __init__(self, x, y, team):
		super().__init__(x, y, team)
		if team == 1:
			self.serialize = 'Q'
		else:
			self.serialize = 'q'

	def print_location(self):
		print("Queen Location in (" + str(self.x) + "," + str(self.y) + ")")

	def get_piece_attacked(self):
		return self.diagonal_piece_attacked(board) + self.horizontal_vertical_piece_attacked(board)

class Knight(Chess):
	def __init__(self, x, y, team):
		super().__init__(x, y, team)
		if team == 1:
			self.serialize = 'K'
		else:
			self.serialize = 'k'

	def print_location(self):
		print("Knight Location in (" + str(self.x) + "," + str(self.y) + ")")

	def get_piece_attacked(self, board):
		return self.l_piece_attacked(board)

class Bishop(Chess):
	def __init__(self, x, y, team):
		super().__init__(x, y, team)
		if team == 1:
			self.serialize = 'B'
		else:
			self.serialize = 'b'

	def print_location(self):
		print("Bishop Location in (" + str(self.x) + "," + str(self.y) + ")")

	def get_piece_attacked(self, board):
		return self.diagonal_piece_attacked(board)

class Rook(Chess):
	def __init__(self, x, y, team):
		super().__init__(x, y, team)
		if team == 1:
			self.serialize = 'R'
		else:
			self.serialize = 'r'

	def print_location(self):
		print("Rook Location in (" + str(self.x) + "," + str(self.y) + ")")

	def get_piece_attacked(self, board):
		return self.horizontal_vertical_piece_attacked(board) 


