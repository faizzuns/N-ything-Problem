from chess import *
from board import Board

def main():
	c1 = Board()
	point = c1.get_random_location()
	queen_black = Queen(point['x'], point['y'],1)
	c1.add_piece(queen_black)
	point = c1.get_random_location()
	knight_black = Knight(point['x'], point['y'],1)
	c1.add_piece(knight_black)
	point = c1.get_random_location()
	bishop_black = Bishop(point['x'], point['y'],1)
	c1.add_piece(bishop_black)
	point = c1.get_random_location()
	rook_black = Rook(point['x'], point['y'],1)
	c1.add_piece(rook_black)

	point = c1.get_random_location()
	queen_white = Queen(point['x'], point['y'],2)
	c1.add_piece(queen_white)
	point = c1.get_random_location()
	knight_white = Knight(point['x'], point['y'],2)
	c1.add_piece(knight_white)
	point = c1.get_random_location()
	bishop_white = Bishop(point['x'], point['y'],2)
	c1.add_piece(bishop_white)
	point = c1.get_random_location()
	rook_white = Rook(point['x'], point['y'],2)
	c1.add_piece(rook_white)
	
	c1.print_board()
	c1.print_piece()


main()