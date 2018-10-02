from os.path import exists
from chess import *
from board import *
import time
import random
import math

def generate_individual():
    c = Board()

    point = c.get_random_location()
    queen_black = Queen(point['x'], point['y'], 'WHITE')
    c.add_piece(queen_black)
    point = c.get_random_location()
    knight_black = Knight(point['x'], point['y'], 'WHITE')
    c.add_piece(knight_black)
    point = c.get_random_location()
    bishop_black = Bishop(point['x'], point['y'], 'WHITE')
    c.add_piece(bishop_black)
    point = c.get_random_location()
    rook_black = Rook(point['x'], point['y'], 'WHITE')
    c.add_piece(rook_black)

    point = c.get_random_location()
    queen_white = Queen(point['x'], point['y'], 'BLACK')
    c.add_piece(queen_white)
    point = c.get_random_location()
    knight_white = Knight(point['x'], point['y'], 'BLACK')
    c.add_piece(knight_white)
    point = c.get_random_location()
    bishop_white = Bishop(point['x'], point['y'], 'BLACK')
    c.add_piece(bishop_white)
    point = c.get_random_location()
    rook_white = Rook(point['x'], point['y'], 'BLACK')
    c.add_piece(rook_white)

    return c

def generate_initial_population(k):
    chess_list = []
    for i in range(k):
        chess = generate_individual()
        chess_list.append(chess)
    print(chess_list)
    return chess_list

# chess_list isinya masih 4 list, terurut dengan chess_list pertama itu yang terbaik
def crossover_function(chess_list):
    new_chess_list = []
    new_chess_list.append(chess_list[0])
    new_chess_list.append(chess_list[1])
    new_chess_list.append(chess_list[1])
    new_chess_list.append(chess_list[2])

    # Algoritma untuk crossing
    for i in range(0,8):
        is_switch = bool(random.getrandbits(1))
        if is_switch:
            if not new_chess_list[1].is_taken(new_chess_list[0].list[i].x, new_chess_list[0].list[i].y) and not new_chess_list[0].is_taken(new_chess_list[1].list[i].x, new_chess_list[1].list[i].y):
                #switch