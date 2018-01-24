from graphics import *
from random import choice

win = GraphWin('Mines', 720, 576)

class MineField(object):
    def __init__(self, dim_x, dim_y):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.mines = []
        for i in range(dim_x):
            print(self.dim_y)
            self.mines.append(self.dim_x * [self.dim_y * ''])

        print(self.mines)
    def Initialize(self):
        for i in range(self.dim_x):
            for a in range(self.dim_y):
                print(i, a)
                mine = choice([True, False])
                self.mines[i][a] = (Mine(i, a, False, False, mine))

class Mine(object):
    def __init__(self, pos_x, pos_y, is_flagged, is_open, has_mine):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_flagged = is_flagged
        self.is_open = is_open
        self.has_mine = has_mine
    def InitSquare(self):
        pass

minefield = MineField(16, 16)
minefield.Initialize()
print(minefield.mines)
for i in minefield.mines:
    for a in i:
        print(a.has_mine)
