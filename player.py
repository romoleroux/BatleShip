# from soupsieve import select
from batleship import Batleship
class Player(Batleship):
    #Constructor
    def __init__(self,level,name):
        super().__init__(level)
        self.name = name

    def placing_bullet(self,bullet_cordenate):
        """This function inside in the  shoot method will check if the buller hit agains a boat"""
        row = bullet_cordenate[0]
        col = bullet_cordenate[1]
        def sunken_chip(row,col):
            """This Function Check if the boat is sink or still is in functionaty.
                Two argos (row , col ) 
                This cordenate wil be use to check if the size of the boat in that location is zero or have any piece.
                """
            for n in self.ship_positions:
                #n[0] ..n[1] etc shows the index value
                #row and col are the limit for the condition, like row must be great than n[0] (INDEX) and less than n[1] (INDEX) row must be in-between
                if n[0] <= row <= n[1] and n[2]<= col <= n[3]:
                    #here we ask if there is any ship, if there is not ship will Return True 
                    if "O" in  self.board[n[0] : n[1] , n[2] : n[3]]:
                        return False
            
            
            return True #The Entrire ship has destroy.
        if self.ship_hit:
            row = self.row_machine
            col = self.col_machine
            if row  - 1 > 0 and self.board[row-1,col] != "%":
                row -= 1
            elif row + 1 < self.board[0].size and self.board[row+1,col] != "%":
                row += 1
            elif col  - 1 > 0 and self.board[row,col-1] != "%":
                col -= 1
            elif col + 1 < self.board[0].size and self.board[row,col+1] != "%":
                col += 1

        if self.board[row,col] == "~":
            self.board[row,col] = "%"
            print("stupid MACHINE you miss the shot!!!")
            return False
        elif self.board[row,col] == "O":
            self.board[row,col] = "X"
            print("greate shot MACHINE!! you hit a boat from this idiot in position:",f"({chr(row).upper()},{col})")
            #Aqui registro la posición del acierto
            # self.ship_bull_cord = [row,col]
            self.row_machine = row
            self.col_machine = col
            self.ship_hit = True
            if sunken_chip(row,col):
                print("Chip destroyed!!!")
                # self.ship_bull_cord.append(row,col)
                self.num_of_ship -= 1
                self.ship_hit = False
            return True
    
    