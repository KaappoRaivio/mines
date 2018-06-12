from graphics import *

# from Mine import *
from Mine import *

# win = GraphWin('Mines', 720, 576)




minefield = MineField(16, 16)
minefield.Initialize()
# for i in minefield.mines:
#     for a in i:
#         print(a.has_mine)
#         print(a.InitSquare())
minefield.PrintPretty()
print(minefield.mines[10][5].AmountOfNeighbors(minefield.mines))
