# from turtle import st

# from platformdirs import user_state_dir
from player import Player
from machine_player import Machine_player

import random

class Game_Logic :
    turns = []
    def __init__(self,player_1,pc_1):
        self.player_1 = player_1 #onjecto de la clase PLayer
        self.pc_1 = pc_1 # objecto de la clase Machine_player

        #variable de que elige random el objeto jugador que empieza 
        self.starter_turn = random.choice([player_1,pc_1])

    def print_boards(self):
        if isinstance(self.turns[0],Player):
            print(self.turns[0].name)
            self.turns[0].print_board()
        else:
            print(self.turns[1].name)
            self.turns[1].print_board()

    #Metodo que imprime tablero rival
    def print_board_pc(self):
        "if que preunta  si la lista turnos tiene la posición de la maquina"
        if isinstance(self.turns[0],Machine_player):
            print("PC PLAYER")
            self.turns[0].print_board_without_my_ships()
        else:
            print("PC PLAYER")
            self.turns[1].print_board_without_my_ships()


    #Crea los baros tanto en jugador maquina como en humano
    def place_ship_board(self):
        self.turns[0].create_ship_board()
        self.turns[1].create_ship_board()
    
    #creación varable turno de tipo lista que guarda datos de tipo objeto, objeto humano, objeto pc
    def create_turns(self):
        if self.starter_turn == self.player_1:
            self.turns = list((self.player_1,self.pc_1))
        else:
            self.turns = list((self.pc_1,self.player_1))

    #metodo que controla turnos, ganador, perdedor, user interface
    def game_running(self):
        i = 0
        #fUNCTION QUE INPUT EL MENSAJE DE LO QUE VAYA A QIERER APLICAR EL UUARIO
        def selection_ok():
            selection_user = input("For playmPrees :\n 1) Shoot\n2) print enemy board :\n3) Exit game!!!\n")
            #IF PARA CONTROLAR QUE SE APORTE LA INFORMACIÓN ESPERADA
            if selection_user.isnumeric():
                if int(selection_user) <= 0 or int(selection_user) > 3:
                    return selection_ok()
            else:
                return selection_ok()
            return  int(selection_user)

        #Cambio de turno
        def change_turn(i):
            if i == 0:
                i = -1
                return i
            else:
                i = 0
                return i

        while True:
            #pregunta si es instancia de la clase PLAYER
            if isinstance(self.turns[i],Player):
                #si es instancia de PLayer print el nombre del jugador en turno
                print(f"----> {self.turns[i].name} TURN <----")
                print(f"Number of ships remind : {self.turns[i].num_of_ship}")
                print("-------------------------------")
                print(f"Number of bullets : {self.turns[i].num_of_bullets}")
                
                user_select = selection_ok() # Print out the selecion (user intrface)
                if user_select == 1:
                    self.print_boards()
                    #bullet_cord es una lista de cordenas
                    bullet_cord = self.turns[i].shooting() # este mehotdo regresa un valor de cordenadas
                    if self.turns[i+1].placing_bullet(bullet_cord):
                        #WIINER meotd
                        if self.turns[i+1].num_of_ship == 0:
                            
                            # print(f"THE WINNER IS : {self.turns[i+1].name}!!!") 
                            print(f"THE WINNER IS : {self.turns[i].name}!!!") 
                            print("you shoul be on the NASA after winning")
                            break
                    #change of turn 
                    else:
                        i = change_turn(i)
                #selectin 2 compute, lo que courre al elegir 2, print de tablero pc
                elif user_select == 2:
                    self.print_board_pc()

                #selectin 2 compute, lo que courre al elegir 3, SALIR DEL JUEGO
                elif user_select == 3:
                    ("we have a coward on board,,, bye bye 🐔")
                    break

                if self.gamer_over():
                    break
            else:
                print("----> PC TURN <----")
                print(f"Number of ships remind : {self.turns[i].num_of_ship}")
                print(f"Number of bullets : {self.turns[i].num_of_bullets}")
                bullet_cord = self.turns[i].shooting()
                if self.turns[i+1].placing_bullet(bullet_cord): 
                    if self.turns[i+1].num_of_ship == 0:
                        print(f"THE PC WIN FUCKER !!!")
                        print("you shoul GO BACK TO ELEMENTERY SCHOOL")
                        break
                else:
                    i = change_turn(i)

    #Donde se perde, sin Probar.
    def gamer_over(self):
        if isinstance(self.turns[0],Player):
            if self.turns[0].num_of_bullets == 0 or self.turns[0].num_of_ship == 0:
                print("Game over!!!!")
                print("You suck, but no worries you can try again if you dear")
                return True
        else:
            if self.turns[1].num_of_bullets == 0 or self.turns[1].num_of_ship == 0:
                print("Game over!!!!")
                print("You suck, but no worries you can try again if you dear")
                return True

