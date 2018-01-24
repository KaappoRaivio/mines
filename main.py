from graphics import *

win = GraphWin('Mines', 720, 576)

class Mine(object):
    def __init__(self, pos_x, pos_y, is_flagged, is_open, has_mine):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_flagged = is_flagged
        self.is_open = is_open
        self.has_mine = has_mine
    def InitSquare(self):
