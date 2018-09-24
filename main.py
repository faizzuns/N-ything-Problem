from os.path import exists
from chess import *
from board import Board
from SimulatedAnnealing import *
import time

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
		return bidak
	else :
		print ("File not exist.")

def intiateBoard() :
	list_bidak = []
	list_bidak = readFile("catur.txt")
	chess_board = Board()
	for x in list_bidak :
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
	
def main():
	chess = intiateBoard()
	menu(chess)

def menu(chess):
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

	print()
	print()
	print()
	print('Initiate Board :')

	if pil == 1:
		chess.print_board()
		print(chess.summary_attacked())
		hill_climbing(chess.total_evaluation(), 100, chess)
		chess.print_board()
		print(chess.summary_attacked())
	elif pil == 2:
		max_iterate = 1000
		temperature = 10000
		descent = 35
		simulate(chess, max_iterate, temperature, descent)
	else:
		# Genetic Algorithm
		print(pil)

def hill_climbing(evals, max_iterate, board):
	current_eval = evals
	for i in range(max_iterate):
		listofval = []
		for piece in board.list:
			result = piece.get_max_trial_value(board)
			listofval.append([result['max_x'],result['max_y'],result['max_eval'],piece])
		optimum = board.get_optimum_movement(listofval)
		
		piece = optimum['piece']
		max_x = optimum['max_x']
		max_y = optimum['max_y']
		saved_x = piece.x
		saved_y	= piece.y
		piece.move_piece(max_x,max_y)
		if current_eval < board.total_evaluation():
			current_eval = board.total_evaluation()
		else:
			piece.move_piece(saved_x,saved_y)
			break

main()