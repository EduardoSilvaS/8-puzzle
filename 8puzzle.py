import pygame
import os
import time
import random
import sys
import copy

pygame.init()

# variables and constants that'll be used to run the game window ----------------------------------------------------------------------  
WIDTH, HEIGHT = 310, 310
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("8 Puzzle")
bg = pygame.image.load(os.path.join("assets", "background.jpg"))

def main_game():
    run = True
    clock = pygame.time.Clock()
    # WIN.blit(bg, (5,5))
    
    images = [[pygame.image.load(os.path.join("assets", "Macaco01.png")), pygame.image.load(os.path.join("assets", "Macaco02.png")), pygame.image.load(os.path.join("assets", "Macaco03.png"))],
                  [pygame.image.load(os.path.join("assets", "Macaco04.png")), pygame.image.load(os.path.join("assets", "Macaco05.png")), pygame.image.load(os.path.join("assets", "Macaco06.png"))],
                  [pygame.image.load(os.path.join("assets", "Macaco07.png")), pygame.image.load(os.path.join("assets", "Macaco08.png")), "x"]]

    img_matrix = [[1,2,3],[4,5,6],[7,8,'x']]
    states = []
    states.append(copy.deepcopy(img_matrix))
    solved = False

    # functions that'll be used in the game ------------------------------------------------------------------------------------------

    def decimal_in_string(string):
        char = 0
        for i in range(len(string)):
            char = string[i]
            if char.isdigit():
                char = int(char)
        return char

    # Function to check if a point is within a rectangle
    def is_point_in_rect(point, rect):
        px, py = point
        rx, ry, rw, rh = rect
        return rx <= px <= rx + rw and ry <= py <= ry + rh
    
    def flatten(matrix):
        return [num for row in matrix for num in row]

    def unflatten(flat_list, rows, cols):
        return [flat_list[i * cols:(i + 1) * cols] for i in range(rows)]

    def is_solvable(matrix):
        flat_list = flatten(matrix)
        inversions = 0
        for i in range(len(flat_list)):
            for j in range(i + 1, len(flat_list)):
                if flat_list[i] != 'x' and flat_list[j] != 'x' and flat_list[j] > flat_list[i]:
                    inversions += 1
        return inversions % 2 == 0
    
    def scramble_matrix(matrix):
        rows, cols = len(matrix), len(matrix[0])
        flat_list = flatten(matrix)
        while True:
            random.shuffle(flat_list)
            new_matrix = unflatten(flat_list, rows, cols)
            if is_solvable(new_matrix):
                print("solucionavel")
                return new_matrix

    # Function to draw the images on the screen and store their positions
    def draw_images():
        image_positions = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(img_matrix)):
            for j in range(len(img_matrix[i])):
                pos = (j*100+5, i*100+5)
                match img_matrix[i][j]:
                    case 1:
                        WIN.blit(images[0][0], pos)
                        image_positions[i][j] = (images[0][0], pos[0], pos[1], 100, 100)
                    case 2:
                        WIN.blit(images[0][1], pos)
                        image_positions[i][j] = (images[0][1], pos[0], pos[1], 100, 100)
                    case 3:
                        WIN.blit(images[0][2], pos)
                        image_positions[i][j] = (images[0][2], pos[0], pos[1], 100, 100)
                    case 4:
                        WIN.blit(images[1][0], pos)
                        image_positions[i][j] = (images[1][0], pos[0], pos[1], 100, 100)
                    case 5:
                        WIN.blit(images[1][1], pos)
                        image_positions[i][j] = (images[1][1], pos[0], pos[1], 100, 100)
                    case 6:
                        WIN.blit(images[1][2], pos)
                        image_positions[i][j] = (images[1][2], pos[0], pos[1], 100, 100)
                    case 7:
                        WIN.blit(images[2][0], pos)
                        image_positions[i][j] = (images[2][0], pos[0], pos[1], 100, 100)
                    case 8:
                        WIN.blit(images[2][1], pos)
                        image_positions[i][j] = (images[2][1], pos[0], pos[1], 100, 100)
                    case 'x':
                        pos = (j*100+5, i*100+5)
                        pygame.draw.rect(WIN, (0, 0, 0), (pos[0], pos[1], 100, 100))
                        image_positions[i][j] = ('x', pos[0], pos[1], 100, 100)           

        return image_positions

    def move_img(img):
        indice = 999
        if img == images[0][0]:
            indice = 1
        elif img == images[0][1]:
            indice = 2
        elif img == images[0][2]:
            indice = 3
        elif img == images[1][0]:
            indice = 4
        elif img == images[1][1]:
            indice = 5
        elif img == images[1][2]:
            indice = 6
        elif img == images[2][0]:
            indice = 7
        elif img == images[2][1]:
            indice = 8

        for i in range(len(img_matrix)):
            for j in range(len(img_matrix[i])):
                if img_matrix[i][j] == indice:
                    if i-1 >= 0 and img_matrix[i-1][j] == 'x':
                        img_matrix[i-1][j] = img_matrix[i][j]
                        img_matrix[i][j] = 'x'
                        return
                    elif i+1 < len(img_matrix) and img_matrix[i+1][j] == 'x':
                        img_matrix[i+1][j] = img_matrix[i][j]
                        img_matrix[i][j] = 'x'
                        return
                    elif j-1 >= 0 and img_matrix[i][j-1] == 'x':
                        img_matrix[i][j-1] = img_matrix[i][j]
                        img_matrix[i][j] = 'x'
                        return
                    elif j+1 < len(img_matrix[i]) and img_matrix[i][j+1] == 'x':
                        img_matrix[i][j+1] = img_matrix[i][j]
                        img_matrix[i][j] = 'x'
                        return

    # Function to handle mouse click events
    def handle_click(image_positions):
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(image_positions)):
            for j in range(len(image_positions[i])):
                if is_point_in_rect(mouse_pos, (image_positions[i][j][1], image_positions[i][j][2], 100, 100)):
                    move_img(image_positions[i][j][0])
                    states.append(copy.deepcopy(img_matrix))
                    return # Adiciona um return para sair da função após detectar um clique

    img_matrix = scramble_matrix(img_matrix) #scramble the matrix before the game starts
    states.append(copy.deepcopy(img_matrix))

    while run:
        clock.tick(60)  # Ajusta a taxa de atualização para 60 FPS
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Detecta cliques do mouse
                handle_click(image_positions)
                print(f"Solved?:{solved}")

        if img_matrix == states[0]:
            WIN.blit(pygame.image.load(os.path.join("assets", "background.jpg")), (5,5))
            states.pop(0)
            solved = True
            print(f"Solved?:{solved}")
            print("You won!")
            print(f"Moves:{len(states)-1}")
            print(f"States: {states}")
            pygame.display.update()  # update screen
            pygame.time.wait(5000)  # Pausa por 10 segundos (10000 milissegundos)
            run = False
        else: 
            image_positions = draw_images()

        pygame.display.update()  # update screen

main_game()

