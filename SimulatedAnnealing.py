from os.path import exists
from chess import *
from board import Board
import time

def simulate(chess, max_iterate, temperature, descent):
	for x in range(max_iterate):
		print()
