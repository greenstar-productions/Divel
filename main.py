import pygame
import player

# Initialization
pygame.init()

window = pygame.display.set_mode((1500, 1250))

pygame.display.set_caption("Divel, a dungeon crawler written in python")

class player:
    class main_player:
        x = 250
        y = 125

while True:
    for event in pygame.event:
        if event.type == pygame.QUIT:
            pygame.quit

# De-Initialization
pygame.quit()
