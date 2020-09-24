import pygame
import player

# Initialization
pygame.init()

window = pygame.display.set_mode((1500, 1250))

pygame.display.set_caption("Divel, a dungeon crawler written in python")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

# De-Initialization
pygame.quit()
