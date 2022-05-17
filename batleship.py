import numpy as np
import random
import math

class Batleship:
    #CLASS ATRIBUTES
    #PRIVATE CLASS
    ship_positions = []
    def __init__(self,level):
        #private member self board using : __
        self.board = np.full((10,10),"~")
        self.ship_hit = False
        self.num_of_ship = 10
        self.level = level
        self.alphabet = "ABCDEFGHIJK"
        self.row_machine = 0
        self.col_machine = 0
        self.num_of_bullets = 30
        

    def print_board(self):
        """This Method will ouput the board game when you call it, not argument need it"""
        
        
        "alphabe will be created using for range :)"
        # for n in range(65,91):
        #     self.alphabet += chr(n)


        # # cut the len of alphabet at the board len
        # self.alphabet = self.alphabet[0 : self.board[0].size + 1]

        print("  ",end=" ")
        for i in range(self.board[0].size):
            print(str(i),end=" ")
        print()
        
        #for to colocate leters and number cordenate, and chips.
        for row in range(self.board[0].size):
            print(self.alphabet[row],end="  ")
            for col in range(self.board[0].size):
                if self.board[row,col] == "O":
                    print("O",end=" ")
                else:
                    print(self.board[row,col],end=" ")
            print()
        
                    
        # for n in self.board:
        #     print(' '.join(n))

        #Clear_oput at every time this method is call
        # clear_output(wait=True)

    def create_ship_board(self):
        """Method that create and collocate the ships on the board in a random way"""
        def place_ship_on_board(row,col,orientation,ship_size):
            """THIs functions will take (row ,col, orientation, ship_size) for check if the ships are insido on the board, if is not inside will return false if is insido will call another function validate_place_ship"""

            # def validate_place_ship(*args):
            def validate_place_ship(row,col,ship_size,axis):
                """argument takes (row,col,ship_size,axis) with this, this function will check if there any ship were we want to collocate our new ship, at the same time if there is no ship on the index array will collocate a ship. This function return True or False"""

                you_can_place = True
                #axis is x o y
                if axis == 0:
                    j = 0
                    for i in self.board[row:row + 1,col - ship_size + 1 : col + 1]:
                        if i[j] != "~":
                            you_can_place = False
                            break
                        j += 1
                    if you_can_place == True:
                        self.board[row:row + 1,col - ship_size + 1 : col + 1]= "O"
                        #self.ship_position make a list from the position, numeric, index
                        self.ship_positions.append([row,row + 1,col - ship_size + 1, col + 1])
                elif axis == 1:
                    j = 0
                    for i in self.board[row - ship_size + 1 : row + 1,col:col + 1]:
                        #the i was lucky hahaha
                        # print("i :",i)
                        if i != "~":
                            you_can_place = False
                            break
                        j += 1
                    if you_can_place == True:
                        self.board[row - ship_size + 1 : row + 1,col:col + 1]= "O"
                        #self.ship_position make a list from the position, numeric, index
                        self.ship_positions.append([row - ship_size + 1, row + 1,col,col + 1])

                
                return you_can_place
            
            #------ END OF FUNCTION validate_place_ship ----------
            
            initial_row,stop_row,initial_column,stop_column = row,row + 1,col,col + 1
            axis = 0
            #Check the orientation on board, can´t be less than zero  than array size in first row
            if orientation == "west" or orientation == "east":
                #the parameter col must be substract from ship_size cause is gonna the space will occupied on the array a
                if col - ship_size  < 0:
                    return False 

            elif orientation == "north" or orientation == "south":
                axis += 1
                if row - ship_size < 0:
                    return False

            return validate_place_ship(row,col,ship_size,axis)
        # END OF FUNCTION place_ship_on_board
        
        number_ship_in_board = 0
        rows, columns = (self.board[0].size,self.board[0].size)

        while number_ship_in_board != self.num_of_ship:
            rand_row = random.randint(0,rows-1)
            rand_col = random.randint(0,columns - 1)
            orientation = random.choice(["west","north","south","east"])
            #list of size for boats
            ship_size = [1,1,1,1,2,2,2,3,3,4]
            ship_size = ship_size[number_ship_in_board]
            if place_ship_on_board(rand_row,rand_col,orientation,ship_size):
                number_ship_in_board += 1
        #will make the list type from ship_position to an numpy array        
        self.ship_positions =np.array(self.ship_positions)
            
    def shooting(self):
        
        valid_place_bullet = False
        row = ""
        column = ""
        self.num_of_bullets -= 1

        while valid_place_bullet is False:
            position =""
            right_cordenates = False
            position = input("Enter row (A - J) enter column (0 - 9) like B2 : ").upper()

            if  len(position) != 2:
                print("ERROR, please enter position like B3")
            else:
                row = position[0]
                column = position[1]
                if not row.isalpha() or not column.isnumeric():
                    print("ERROR, please enter position like B3")
                else:
                    right_cordenates = True
            if right_cordenates:
                break
                
            
        return [row,column]


    def placing_bullet(self,bullet_cordenate):
        """This function inside in the  shoot method will check if the buller hit agains a boat"""
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

        print(bullet_cordenate)
        row = self.alphabet.index(bullet_cordenate[0])
        col =  int(bullet_cordenate[1])
        # print("row to col :",self.ship_positions[2:3])
        # for pos in self.ship_positions:
            
        # print(self.ship_positions)
        
        if self.board[row,col] == "~":
            self.board[row,col] = "%"
            print("you miss the shot!!!")
            return False
        elif self.board[row,col] == "O":
            self.board[row,col] = "X"
            print("greate shot!! you hit a boat in position:",f"{bullet_cordenate}")
            if sunken_chip(row,col):
                print("Chip destroyed!!!")
                self.num_of_ship -= 1
            return True
        # def placement_bullet():
        #     pass
            # valid_place_bullet = False
            # row = ""
            # column = ""


        
        # print(bullet_cordenate)
            # while valid_place_bullet is False:
            #     position =""
            #     right_cordenates = False
            #     position = input("Enter row (A - J) enter column (0 - 9) like B2 : ").upper()

            #     if len(position) < 0 or len(position) > 2:
            #         print("ERROR, please enter position like B3")
            #         print(len(position))
            #     else:
            #         row = position[0]
            #         column = position[1]
            #         if not row.isalpha or not column.isnumeric:
            #             print("ERROR, please enter position like B3")
            #         else:
            #             right_cordenates = True
            #     print(right_cordenates)
            #     if right_cordenates:
            #         break
            
            # return [row,column]
                    
            # print(self.ship_positions[0,0])
        # print(self.ship_positions[row,col])

        

