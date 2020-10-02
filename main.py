import pygame
import sys
import player

# Initialization
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((1500, 800))

pygame.display.set_caption("Divel, a dungeon crawler written in python")

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game == False
            sys.exit()

# De-Initialization
pygame.quit()
