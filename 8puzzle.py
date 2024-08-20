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
    # WIN.blit(bg, (5,5))
    
    img_matrix = [[pygame.image.load(os.path.join("assets", "Macaco01.png")), pygame.image.load(os.path.join("assets", "Macaco02.png")), pygame.image.load(os.path.join("assets", "Macaco03.png"))],
                  [pygame.image.load(os.path.join("assets", "Macaco04.png")), pygame.image.load(os.path.join("assets", "Macaco05.png")), pygame.image.load(os.path.join("assets", "Macaco06.png"))],
                  [pygame.image.load(os.path.join("assets", "Macaco07.png")), pygame.image.load(os.path.join("assets", "Macaco08.png")),"x"]]

    # functions that'll be used in the game ------------------------------------------------------------------------------------------
    def isClosed(): # check if the game is closed
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return True
        return False

    # Function to check if a point is within a rectangle
    def is_point_in_rect(point, rect):
        px, py = point
        rx, ry, rw, rh = rect
        return rx <= px <= rx + rw and ry <= py <= ry + rh

    # Function to draw the images on the screen and store their positions
    def draw_images():
        image_positions = []
        for i in range(len(img_matrix)):
            for j in range(len(img_matrix[i])):
                if img_matrix[i][j] != 'x':
                    pos = (j*100+5, i*100+5)
                    WIN.blit(img_matrix[i][j], pos)
                    image_positions.append((img_matrix[i][j], pos[0], pos[1], 100, 100))
        return image_positions

    # Function to handle mouse click events
    def handle_click(image_positions):
        mouse_pos = pygame.mouse.get_pos()
        for img, x, y, w, h in image_positions:
            if is_point_in_rect(mouse_pos, (x, y, w, h)):
                print(f"Image at ({x}, {y}) clicked!")


    while run:
        clock.tick(120)
        
        if isClosed():
            run = False
        
        image_positions = draw_images()

        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                handle_click(image_positions)

        pygame.display.update()

main_game()
