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
    def __str__(self):
        temp_string = ''
        for x in self.mines:
            for y in x:
                if y.is_flagged:
                    temp_string += 'F'
                elif y.has_exploded:
                    temp_string += '*'
                elif y.is_open:
                    if str(self.AmountOfNeighbors(y.pos_x, y.pos_y)) == 0:
                        temp_string += '<'
                    else:
                        temp_string += str(self.AmountOfNeighbors(y.pos_x, y.pos_y))
                else:
                    temp_string += 'O'
                temp_string += ' '
            temp_string += ' '
            for y in x:
                if y.has_mine:
                    temp_string += 'X'
                else:
                    temp_string += 'O'
                temp_string += ' '

            temp_string += '\n'
        return temp_string

    def Initialize(self, number_of_mines):
        mine_count = 0
        def randomMine(number_of_mines, amount_of_space):
            if random() < number_of_mines / amount_of_space:
                return True
            else:
                return False
        available_space = self.dim_x * self.dim_y
        for i in range(self.dim_x):
            for a in range(self.dim_y):
                mine = randomMine(number_of_mines, available_space)
                mine_count += int(mine)
                self.mines[a][i] = (Mine(i, a, False, False, False, mine, False))
                #print(i, a)
                available_space -= 1
                number_of_mines -= int(mine)
        print(mine_count)

    def AmountOfNeighbors(self, x, y):
        amount = 0
        for i in self.mines[x][y].neighbors:
            if self.mines[i[0]][i[1]].has_mine == True:
                amount += 1
        #print(amount)
        return amount
    def ClickUnnesessary(self):
        for x in self.mines:
            for y in x:
                #print(y.pos_x, y.pos_y)
                if y.is_open:
                    print('terve')
                if self.AmountOfNeighbors(y.pos_x, y.pos_y) == 0 and y.is_open == True:
                    for i in y.neighbors:
                        self.mines[i[0]][i[1]].is_open = True
class Mine(MineField):
    def __init__(self, pos_x, pos_y, is_flagged, is_opening_pending, is_open, has_mine, has_exploded):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_flagged = is_flagged
        self.is_opening_pending = is_opening_pending
        self.is_open = is_open
        self.has_mine = has_mine
        self.has_exploded = has_exploded
        self.neighbors = [[self.pos_x + 1, self.pos_y], [self.pos_x + 1, self.pos_y + 1], [self.pos_x, self.pos_y + 1], [self.pos_x - 1, self.pos_y + 1 ], [self.pos_x - 1, self.pos_y], [self.pos_x - 1, self.pos_y - 1], [self.pos_x, self.pos_y - 1], [self.pos_x + 1, self.pos_y - 1]]
        to_be_removed = []
        for i in range(len(self.neighbors)):
            for a in self.neighbors[i]:
                if a > 15 or a < 0:
                    to_be_removed.append(self.neighbors[i])
                    break
        for i in to_be_removed:
            self.neighbors.remove(i)
    def InitSquare(self):
        kerroin = 10 #muutettava myöhemmmin vastaamaan ikkunan mittoja.
        return [Point(kerroin * self.pos_x, kerroin * self.pos_y), Point(kerroin * self.pos_x + kerroin, kerroin * self.pos_y + kerroin)]


minefield = MineField(16, 16)
minefield.Initialize(100)
# for i in minefield.mines:
#     for a in i:
#         print(a.has_mine)
#         print(a.InitSquare())

first_run = True

while True:
    print(minefield)
    user_trying_to_flag_mine = False
    guess = input('Arvauksesi (muotoa \"<x>, <y>\"):').split(' ')
    if guess[0].lower() == 'f':
        user_trying_to_flag_mine = True
        guess = guess[1:]

    try:
        for i in range(len(guess)):
            guess[i] = int(guess[i]) - 1
    except:
        print('Inputti ei kelpaa!!!')
    if user_trying_to_flag_mine:
        minefield.mines[guess[1]][guess[0]].is_flagged = not minefield.mines[guess[1]][guess[0]].is_flagged
        first_run = False
        continue
    if not minefield.mines[guess[1]][guess[0]].has_mine:
        minefield.mines[guess[1]][guess[0]].is_open = True

    elif first_run:
        minefield.mines[guess[1]][guess[0]].has_mine = False
        minefield.mines[guess[1]][guess[0]].is_open = True

    else:
        minefield.mines[guess[1]][guess[0]].has_exploded = True
        print(minefield)
        print('Hävisit pelin!')
        quit()

    first_run = False

    minefield.ClickUnnesessary()
