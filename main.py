from chess import *
from board import Board
import time

def main():
	c1 = Board()
	point = c1.get_random_location()
	queen_black = Queen(point['x'], point['y'], 'WHITE')
	c1.add_piece(queen_black)
	point = c1.get_random_location()
	knight_black = Knight(point['x'], point['y'], 'WHITE')
	c1.add_piece(knight_black)
	point = c1.get_random_location()
	bishop_black = Bishop(point['x'], point['y'], 'WHITE')
	c1.add_piece(bishop_black)
	point = c1.get_random_location()
	rook_black = Rook(point['x'], point['y'], 'WHITE')
	c1.add_piece(rook_black)

	point = c1.get_random_location()
	queen_white = Queen(point['x'], point['y'], 'BLACK')
	c1.add_piece(queen_white)
	point = c1.get_random_location()
	knight_white = Knight(point['x'], point['y'], 'BLACK')
	c1.add_piece(knight_white)
	point = c1.get_random_location()
	bishop_white = Bishop(point['x'], point['y'], 'BLACK')
	c1.add_piece(bishop_white)
	point = c1.get_random_location()
	rook_white = Rook(point['x'], point['y'], 'BLACK')
	c1.add_piece(rook_white)

	simulatedAnnealing(c1, 1000, 1000, 10)

def simulatedAnnealing(board, temperature, max_iterate, descent):
	for i in range(max_iterate):
		attack_info = board.summary_attacked()
		selisih = attack_info['opponent'] - attack_info['teamates']
		board.move_one_piece(selisih, temperature)
		if i == 0 or i == max_iterate - 1:
			print(attack_info)
		if temperature > 0:
			temperature = temperature - descent

start = time.time()
main()
finish = time.time() - start
print('Compile Time : ' + finish)