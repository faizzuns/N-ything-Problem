from os.path import exists
from chess import *
from board import Board
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
	chess.print_board()
	chess.print_info()

	if pil == 1:
		hill_climbing(chess.total_evaluation(),100,chess)
		chess.print_board()
		chess.print_info()
		print(pil)
	elif pil == 2:
		# Simulated Annealing
		print(pil)
	else:
		# Genetic Algorithm
		print(pil)

def hill_climbing(evals,maxIterate,board):
	
	current_eval = evals
	for i in range(maxIterate):
		print("iteration :", i)
		listofval = []
		for piece in board.list:
			result = piece.get_max_trial_value(board)
			listofval.append([result['max_x'],result['max_y'],result['max_eval'],piece])
		optimum = board.get_optimum_movement(listofval)
		print("current eval :", current_eval)
		
		piece = optimum['piece']
		max_x = optimum['max_x']
		max_y = optimum['max_y']
		saved_x = piece.x
		saved_y	= piece.y
		piece.move_piece(max_x,max_y)
		print("board evaluation: ", board.total_evaluation())
		print ("total :")
		print ("teammates: ", board.total_attack()['teammates'])
		print("opponents: ",board.total_attack()['opponents'])
		if current_eval < board.total_evaluation():
			print("masuk ke evaluasi")
			current_eval = board.total_evaluation()
			
			print("iteration :", i)
		else:
			print("ke break")
			piece.move_piece(saved_x,saved_y)
			break

	total = board.total_attack()
	#print("Finish calculating hill climbing")
	#print ("hasil :")
	#print("teammates attacked :", total['teammates'])
	#print("opponents attacked :", total['opponents'])


main()