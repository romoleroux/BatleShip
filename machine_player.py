from typing import overload
from batleship import Batleship
from random import randint
import numpy as np

class Machine_player(Batleship):
    def __init__(self, level,human_player):
        super().__init__(level)
        self.ship_bull_cord = np.full((10,10)," ")

    def print_board_without_my_ships(self):
        board_with_not_chips = self.board.copy()
        print("  ",end=" ")
        for i in range(board_with_not_chips[0].size):
            print(str(i),end=" ")
        print()
        
        #for to colocate leters and number cordenate, and chips.
        for row in range(board_with_not_chips[0].size):
            print(self.alphabet[row],end="  ")
            for col in range(board_with_not_chips[0].size):
                if board_with_not_chips[row,col] == "O":
                    print("~",end=" ")
                    # print("O",end=" ")
                else:
                    print(board_with_not_chips[row,col],end=" ")
            print()

    def shooting(self):
        self.num_of_bullets -= 1
        if self.ship_hit == False:
            row = randint(0,9)
            col = randint(0,9)
            while True:
                if self.ship_bull_cord[row,col] != "X" or self.ship_bull_cord[row,col] != "%":
                    break
                else:
                    row = randint(0,9)
                    col = randint(0,9)
    
        return [row,col]
