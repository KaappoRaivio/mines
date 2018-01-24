from graphics import *
from random import random

#win = GraphWin('Mines', 720, 576)

class MineField(object):
    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.mines = []
        for i in range(1, dim_x + 1):
            self.mines.append(self.dim_x * [self.dim_y * ''])

    def Initialize(self):
        for i in range(self.dim_x):
            for a in range(self.dim_y):
                mine = choice([True, False])
                self.mines[a][i] = (Mine(i, a, False, False, mine, False))

    def PrintPretty(self):
        quit = False
        for i in self.mines:
            row = ''
            for a in i:
                if a.is_open == True:
                    row += str(self.AmountOfNeighbors(a.pos_x, a.pos_y))
                elif a.has_exploded == True:
                    quit = True
                    row += '*'
                else:
                    row += 'O'
                row += ' '
            print(row)
        if quit:
            print('Hävisit pelin!')
            return -1


    def AmountOfNeighbors(self, x, y):
        amount = 0
        for i in self.mines[x][y].neighbors:
            if self.mines[i[0]][i[1]].has_mine == True:
                amount += 1
        return amount
class Mine(MineField):
    def __init__(self, pos_x, pos_y, is_flagged, is_open, has_mine, has_exploded):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_flagged = is_flagged
        self.is_open = is_open
        self.has_mine = has_mine
        self.has_exploded = has_exploded
        self.neighbors = [[self.pos_x + 1, self.pos_y], [self.pos_x + 1, self.pos_y - 1], [self.pos_x, self.pos_y - 1], [self.pos_x - 1, self.pos_y - 1 ], [self.pos_x - 1, self.pos_y], [self.pos_x - 1, self.pos_y + 1], [self.pos_x, self.pos_y + 1], [self.pos_x + 1, self.pos_y + 1]]
    def InitSquare(self):
        kerroin = 10 #muutettava myöhemmmin vastaamaan ikkunan mittoja.
        return [Point(kerroin * self.pos_x, kerroin * self.pos_y), Point(kerroin * self.pos_x + kerroin, kerroin * self.pos_y + kerroin)]


minefield = MineField(16, 16)
minefield.Initialize()
# for i in minefield.mines:
#     for a in i:
#         print(a.has_mine)
#         print(a.InitSquare())
minefield.PrintPretty()
print(minefield.AmountOfNeighbors(14, 11))

while True:
    if minefield.PrintPretty() == -1:
        break
    guess = input('Arvauksesi (muotoa \"<x>, <y>\"):').split(', ')
    try:
        for i in range(len(guess)):
            guess[i] = int(guess[i]) - 1
    except ValueError:
        print('Inputti ei kelpaa!!!')
    if not minefield.mines[guess[1]][guess[0]].has_mine:
        minefield.mines[guess[1]][guess[0]].is_open = True
    else:
        minefield.mines[guess[1]][guess[0]].has_exploded = True
