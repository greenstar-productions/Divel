import pygame
import player.py

# Initialization
pygame.init()

window = pygame.display.set_mode((500, 250))

pygame.display.set_caption("Divel, a dungeon crawler written in python")

class player:
    class main_player:
        x = 250
        y = 125

#while game_running:
#   blah blah code stuff

# De-Initialization
pygame.quit()
