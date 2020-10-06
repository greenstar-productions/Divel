import pygame
import sys
import player

# Initialization
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((150https://www.youtube.com/watch?v=lOeIDvyRUQs0, 800))
font = pygame.font.Font("Inter-Thin.otf", 15)

pygame.display.set_caption("Divel, a dungeon crawler written in python")

game = True
def main_menu():
    while game:
        # button stuff ane things
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game == False
                sys.exit()

# De-Initialization
    pygame.quit()

if __name__ == '__main__':
    main_menu()
