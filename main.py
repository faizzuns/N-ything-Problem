from os.path import exists
from chess import *
from board import Board

def readFile(filename) :
	if exists(filename) :
		file = open(filename,"r")
		row = 8
		chess = []
		for i in range(row) :
			chess.append(file.readline().replace('\n',''))

		bidak = []
		for x in chess :
			bidak.append(x.split(' '))

		print (bidak)
		return bidak
	else :
		print ("File not exist.")

def intiateBoard() :
	list_bidak = []
	list_bidak = readFile("catur.txt")
	chess_board = Board()
	for x in list_bidak :
		point = chess_board.get_random_location()
		if (x[1] == 'KNIGHT') :
			for i in range(int(x[2])) :
				point = chess_board.get_random_location()
				if (x[0] == 'WHITE') :
					white_knight = Knight(point['x'],point['y'],'WHITE')
					chess_board.add_piece(white_knight)
				else :
					black_knight = Knight(point['x'],point['y'],'BLACK')
					chess_board.add_piece(black_knight)
		elif (x[1] == 'BISHOP') :
			for i in range(int(x[2])) :
				point = chess_board.get_random_location()
				if (x[0] == 'WHITE') :
					white_bishop = Bishop(point['x'],point['y'],'WHITE')
					chess_board.add_piece(white_bishop)
				else:
					black_bishop = Bishop(point['x'],point['y'],'BLACK')
					chess_board.add_piece(black_bishop)
		elif (x[1] == 'QUEEN') :
			for i in range(int(x[2])) :
				point = chess_board.get_random_location()
				if (x[0] == 'WHITE') :
					white_queen = Queen(point['x'],point['y'],'WHITE')
					chess_board.add_piece(white_queen)
				else :
					black_queen = Queen(point['x'],point['y'],'BLACK')
					chess_board.add_piece(black_queen)
		elif (x[1] == 'ROOK') :
			for i in range(int(x[2])) :
				point = chess_board.get_random_location()
				if (x[0] == 'WHITE') :
					white_rook = Rook(point['x'],point['y'],'WHITE')
					chess_board.add_piece(white_rook)
				else : 
					black_rook = Rook(point['x'],point['y'],'BLACK')
					chess_board.add_piece(black_rook)

	return chess_board

chess = intiateBoard()
chess.print_board()
chess.print_piece()
chess.print_info()
# main()
