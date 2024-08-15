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

