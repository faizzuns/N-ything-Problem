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
	same = 0
	chess.print_board()
	summary_attacked = chess.summary_attacked()
	print('summary_attacked :', summary_attacked)
	print()

	for x in range(max_iterate):
		worst_piece = find_worst_piece(chess)
		worst_piece_x = worst_piece.x
		worst_piece_y = worst_piece.y
		worst_piece_diff = chess.get_attacked_difference(worst_piece)
		sum_diff = summary_attacked['opponents'] - summary_attacked['teamates']
		location = chess.get_random_location()
		worst_piece.x = location['x']
		worst_piece.y = location['y']
		new_sum_atk = chess.summary_attacked()
		new_sum_diff = new_sum_atk['opponents'] - new_sum_atk['teamates']

		if (chess.get_attacked_difference(worst_piece) < worst_piece_diff or new_sum_diff < sum_diff) and temperature != 0:
			delta_E = chess.get_attacked_difference(worst_piece) - worst_piece_diff
			probability = math.exp(delta_E/temperature)
			random_number = random.random()

			if (random_number > probability):
				worst_piece.x = worst_piece_x
				worst_piece.y = worst_piece_y

		temperature = temperature - descent

	print('Result :')
	chess.print_board()
	print('summary_attacked :', chess.summary_attacked())

