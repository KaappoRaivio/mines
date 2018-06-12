from random import choice

class Mine:
    def __init__(self, pos_x, pos_y, is_flagged, is_open, has_mine):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_flagged = is_flagged
        self.is_open = is_open
        self.has_mine = has_mine
        self.neighbors = [[self.pos_x + 1, self.pos_y], [self.pos_x + 1, self.pos_y - 1], [self.pos_x, self.pos_y - 1], [self.pos_x - 1, self.pos_y - 1 ], [self.pos_x - 1, self.pos_y], [self.pos_x - 1, self.pos_y + 1], [self.pos_x, self.pos_y + 1], [self.pos_x + 1, self.pos_y + 1]]

    def AmountOfNeighbors(self, list_of_mines):
        amount = 0
        for i in self.neighbors:
            if list_of_mines[i[0]][i[1]].has_mine == True:
                amount += 1
        return amount

    def InitSquare(self):
        kerroin = 10 #muutettava myöhemmmin vastaamaan ikkunan mittoja.
        return [Point(kerroin * self.pos_x, kerroin * self.pos_y), Point(kerroin * self.pos_x + kerroin, kerroin * self.pos_y + kerroin)]




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
                self.mines[a][i] = (Mine(i, a, False, False, mine))

    def PrintPretty(self):
        for i in self.mines:
            row = ''
            for a in i:
                if a.has_mine == True:
                    row += '1'
                else:
                    row += '0'
                row += ' '
            print(row)
