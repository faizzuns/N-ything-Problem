from os.path import exists
from chess import *
from board import Board
import random
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

def fitnessFunction(board) :
	count_team = 0
	count_opponent = 0
	fitness_count = 0
	for piece in board.list :
		attack = piece.count_piece_attacked(board)
		count_team += attack[piece.team]
		count_opponent += attack[piece.get_opponent()]

	fitness_count = count_team - count_opponent
	return (fitness_count)

def generatePopulation(population_number) :
	populations = []
	for i in range(population_number) :
		chess = intiateBoard()
		populations.append(chess)

	return populations

def SortAlgorithm(populations) :
	fitness_list = []
	iterate = 1
	print ("Population in Genetic Algorithm : ")
	for population in populations :
		print ("Board", iterate)
		fitness_count = fitnessFunction(population)
		fitness_list.append([population,fitness_count])
		population.print_board()
		print ("Nilai fitness function : ", fitness_count)
		iterate += 1

	sort_list = []
	sort_list = sorted(fitness_list, key=lambda fitness : fitness[1], reverse=True)

	return (sort_list)

def crossoverFunction(sorted_list):
	# Membuat board population untuk generasi selanjutnya
	new_population_board = []
	new_population_board.append(sorted_list[0][0])
	new_population_board.append(sorted_list[1][0])
	new_population_board.append(sorted_list[1][0])
	new_population_board.append(sorted_list[2][0])

	jumlah_bidak = len(sorted_list[0][0].list)

	# Crossing pasangan pertama
	for i in range(jumlah_bidak):
		if bool(random.randint(0,1)):
			# tuker
			# cek apakah bentrok atau enggak
			x_bidak_board_0 = new_population_board[0].list[i].x
			y_bidak_board_0 = new_population_board[0].list[i].y
			x_bidak_board_1 = new_population_board[1].list[i].x
			y_bidak_board_1 = new_population_board[1].list[i].y
			if (new_population_board[0].is_taken(x_bidak_board_1, y_bidak_board_1) or new_population_board[1].is_taken(x_bidak_board_0, y_bidak_board_0)):
				rand_point_0 = new_population_board[0].get_random_location()
				rand_point_1 = new_population_board[1].get_random_location()
				if new_population_board[0].is_taken(x_bidak_board_1, y_bidak_board_1) and new_population_board[1].is_taken(x_bidak_board_0, y_bidak_board_0):
					new_population_board[0].list[i].x = rand_point_0['x']
					new_population_board[0].list[i].y = rand_point_0['y']
					new_population_board[1].list[i].x = rand_point_1['x']
					new_population_board[1].list[i].y = rand_point_1['y']
				elif new_population_board[0].is_taken(x_bidak_board_1, y_bidak_board_1):
					new_population_board[0].list[i].x = rand_point_0['x']
					new_population_board[0].list[i].y = rand_point_0['y']
					new_population_board[1].list[i].x = x_bidak_board_0
					new_population_board[1].list[i].y = y_bidak_board_0
				else:
					new_population_board[0].list[i].x = x_bidak_board_1
					new_population_board[0].list[i].y = y_bidak_board_1
					new_population_board[1].list[i].x = rand_point_1['x']
					new_population_board[1].list[i].y = rand_point_1['y']
			else:
				new_population_board[0].list[i].x = x_bidak_board_1
				new_population_board[0].list[i].y = y_bidak_board_1
				new_population_board[1].list[i].x = x_bidak_board_0
				new_population_board[1].list[i].y = y_bidak_board_0

	# Crossing pasangan kedua
	for i in range(jumlah_bidak):
		if bool(random.randint(0,1)):
			# tuker
			# cek apakah bentrok atau enggak
			x_bidak_board_2 = new_population_board[2].list[i].x
			y_bidak_board_2 = new_population_board[2].list[i].y
			x_bidak_board_3 = new_population_board[3].list[i].x
			y_bidak_board_3 = new_population_board[3].list[i].y
			if (new_population_board[2].is_taken(x_bidak_board_3, y_bidak_board_3) or new_population_board[3].is_taken(x_bidak_board_2, y_bidak_board_2)):
				rand_point_2 = new_population_board[2].get_random_location()
				rand_point_3 = new_population_board[3].get_random_location()
				if new_population_board[2].is_taken(x_bidak_board_3, y_bidak_board_3) and new_population_board[3].is_taken(x_bidak_board_2, y_bidak_board_2):
					new_population_board[2].list[i].x = rand_point_2['x']
					new_population_board[2].list[i].y = rand_point_2['y']
					new_population_board[3].list[i].x = rand_point_3['x']
					new_population_board[3].list[i].y = rand_point_3['y']
				elif new_population_board[2].is_taken(x_bidak_board_3, y_bidak_board_3):
					new_population_board[2].list[i].x = rand_point_2['x']
					new_population_board[2].list[i].y = rand_point_2['y']
					new_population_board[3].list[i].x = x_bidak_board_2
					new_population_board[3].list[i].y = y_bidak_board_2
				else:
					new_population_board[2].list[i].x = x_bidak_board_3
					new_population_board[2].list[i].y = y_bidak_board_3
					new_population_board[3].list[i].x = rand_point_3['x']
					new_population_board[3].list[i].y = rand_point_3['y']
			else:
				new_population_board[2].list[i].x = x_bidak_board_3
				new_population_board[2].list[i].y = y_bidak_board_3
				new_population_board[3].list[i].x = x_bidak_board_2
				new_population_board[3].list[i].y = y_bidak_board_2

	return new_population_board

def geneticAlgorithm(populations, n):
	result_populations = []
	for i in range(n+1):

		sort_list = []
		sort_list = SortAlgorithm(populations)

		if (i != n):
			new_population_list = []
			new_population_list = crossoverFunction(sort_list)
			result_populations = new_population_list

	return (result_populations)

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
		populations = []
		results = []
		results_genetic = []
		populations = generatePopulation(4)
		results = geneticAlgorithm(populations,10)
		results_genetic = SortAlgorithm(results)
		result = results_genetic[0]
		print ("Hasil dari Genetic Algorithm ialah : ")
		print ("Nilai Fitness Function : ")
		print (result[1])
		result[0].print_board()
		result[0].print_info()

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
