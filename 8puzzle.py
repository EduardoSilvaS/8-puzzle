import pygame
import os
import time
import random
import sys

pygame.init()

# variables and constants that'll be used to run the game window ----------------------------------------------------------------------
WIDTH, HEIGHT = 310, 310  
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("8 Puzzle")
bg = pygame.image.load(os.path.join("assets", "background.jpg"))

def main_game():
    run = True
    clock = pygame.time.Clock()
    WIN.blit(bg, (5,5))
    
    img_matrix = [[pygame.image.load(os.path.join("assets", "Macaco01.png")), pygame.image.load(os.path.join("assets", "Macaco02.png")), pygame.image.load(os.path.join("assets", "Macaco03.png"))],
                  [pygame.image.load(os.path.join("assets", "Macaco04.png")), pygame.image.load(os.path.join("assets", "Macaco05.png")), pygame.image.load(os.path.join("assets", "Macaco06.png"))],
                  [pygame.image.load(os.path.join("assets", "Macaco07.png")), pygame.image.load(os.path.join("assets", "Macaco08.png")),"x"]]

    # functions that'll be used in the game ------------------------------------------------------------------------------------------
    def isClosed(): # check if the game is closed
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return True
        return False

    while run:
        clock.tick(120)
        
        if isClosed():
            run = False

        pygame.display.update()

main_game()
