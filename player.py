import pygame

class player:
    class main_player:
        x = 250
        y = 125
        def move(button):
            if button == 1:
                x -= 1
            if button == 2:
                y -= 1
            if button == 3:
                x += 1
            if button == 4:
                y += 1
    class other_player:
        def __init__(x, y):
            raise
