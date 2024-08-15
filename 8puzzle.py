import pygame
import os
import time
import random
import sys

pygame.init()

# variables and constants that'll be used to run the game window ----------------------------------------------------------------------
WIDTH, HEIGHT = 720, 720  
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("8 Puzzle")
background = Background(WIDTH, HEIGHT, pygame.image.load(os.path.join("assets", "background.jpg")), WIN)

def main_game():
    run = True
    clock = pygame.time.Clock()

    # functions that'll be used in the game ------------------------------------------------------------------------------------------
    def isClosed(): # check if the game is closed
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return True
        return False

    while run:
        clock.tick(120)
        
        if isClosed():
            pygame.quit()
            run = False

        pygame.display.update()

main_game()
