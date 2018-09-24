from os.path import exists
from chess import *
from board import *
import time
import random
import math

def find_worst_piece(chess):
	x = chess.list[0]

	for bidak in chess.list:
		if chess.get_attacked_difference(x) > chess.get_attacked_difference(bidak):
			x = bidak

	return x

def simulate(chess, max_iterate, temperature, descent):
	chess.print_board()
	print('summary_attacked :', chess.summary_attacked())
	print('summary_board_attacked :', )

	for x in range(max_iterate):
		worst_piece = find_worst_piece(chess)
		worst_piece_x = worst_piece.x
		worst_piece_y = worst_piece.y
		worst_piece_diff = chess.get_attacked_difference(worst_piece)
		location = chess.get_random_location()
		worst_piece.x = location['x']
		worst_piece.y = location['y']

		if (chess.get_attacked_difference(worst_piece) <= worst_piece_diff) and temperature != 0:
			delta_E = chess.get_attacked_difference(worst_piece) - worst_piece_diff
			probability = math.exp(delta_E/temperature)
			random_number = random.random()

			if (random_number > probability):
				worst_piece.x = worst_piece_x
				worst_piece.y = worst_piece_y

		temperature = temperature - descent

	chess.print_board()
	print('summary_attacked :', chess.summary_attacked())

