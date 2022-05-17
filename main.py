import random
from game_logic import Game_Logic
from player import Player
from machine_player import  Machine_player

#----->aqui se puede escribir mensaje de bienvenida<--------
#          EJEMPLO
#---> Bienvenido a Hundir la Flota <----
# Simbolos : ~ olas, X aciertas, O botes
#Buena suerte, LA MÁQUINA ES MUY DIFICIL JAJAA.
#* Aqui puede escribir lo que quieras.


#* Esta variable pregunta por el nombre del jugador
player_name = input("Please enter your name : ")

player_1 = Player("normal",player_name)
pc_player = Machine_player("normal",player_1)
game = Game_Logic(player_1,pc_player)

game.create_turns()
game.place_ship_board()
game.print_boards()
game.game_running() #<------ metodo que corre el juego con el while





