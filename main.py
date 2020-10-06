import pygame
import sys
import player

# Initialization
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
font = pygame.font.Font("undefined-medium.ttf", 20)
pygame.display.set_caption("Divel, a dungeon crawler written in python")

# variables
game = True
click = False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while game:
        # button stuff and things
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game == False
                sys.exit()


# De-Initialization
    pygame.quit()

if __name__ == '__main__':
    main_menu()
