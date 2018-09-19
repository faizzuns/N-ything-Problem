from chess import *
from board import Board

def menu():

	print(' _____            _    _    _              _____            _    _             ')
	print('|   | | ___  _ _ | |_ | |_ |_| ___  ___   |  _  | ___  ___ | |_ | | ___  _____ ')
	print('| | | ||___|| | ||  _||   || ||   || . |  |   __||  _|| . || . || || -_||     |')
	print('|_|___|     |_  ||_|  |_|_||_||_|_||_  |  |__|   |_|  |___||___||_||___||_|_|_|')
	print('            |___|                  |___|                                       ')
	print()
	print()
	print('PILIH ALGORITMA LOCAL SEARCH :')
	print('1. Hill Climbing')
	print('2. Simulated Annealing')
	print('3. Genetic Algorithm')
	print('Your Choice : ', end ='')
	pil = int(input())

	while (pil < 1) or (pil > 3):
		print('Invalid input, please try again.')
		print('Your Choice : ', end='')
		pil = int(input())

	return pil


def main():
	X = menu()
	
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

	c1.print_board()
	c1.print_piece()
	c1.print_info()


main()