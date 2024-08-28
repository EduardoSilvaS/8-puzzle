import pygame
import os
import time
import random
import sys

pygame.init()

# Variáveis e constantes que serão usadas para executar a janela do jogo
WIDTH, HEIGHT = 310, 310
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("8 Puzzle")
bg = pygame.image.load(os.path.join("assets", "background.jpg"))

def main_game():
    run = True
    clock = pygame.time.Clock()
    
    img_matrix = [[pygame.image.load(os.path.join("assets", "Macaco01.png")), pygame.image.load(os.path.join("assets", "Macaco02.png")), pygame.image.load(os.path.join("assets", "Macaco03.png"))],
                  [pygame.image.load(os.path.join("assets", "Macaco04.png")), pygame.image.load(os.path.join("assets", "Macaco05.png")), pygame.image.load(os.path.join("assets", "Macaco06.png"))],
                  [pygame.image.load(os.path.join("assets", "Macaco07.png")), pygame.image.load(os.path.join("assets", "Macaco08.png")), "x"]]

    # Funções que serão usadas no jogo
    def isClosed():  # Verifica se o jogo foi fechado
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return True
        return False

    def decimal_in_string(string):
        char = 0
        for i in range(len(string)):
            char = string[i]
            if char.isdigit():
                char = int(char)
        return char

    # Função para verificar se um ponto está dentro de um retângulo
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
                if flat_list[i] != 'x' and flat_list[j] != 'x' and decimal_in_string(str(flat_list[j])) < decimal_in_string(str(flat_list[i])):
                    inversions += 1
        return inversions % 2 == 0
    
    def scramble_matrix(matrix):
        rows, cols = len(matrix), len(matrix[0])
        flat_list = flatten(matrix)
        while True:
            random.shuffle(flat_list)
            new_matrix = unflatten(flat_list, rows, cols)
            if is_solvable(new_matrix):
                return new_matrix

    # Função para desenhar as imagens na tela e armazenar suas posições
    def draw_images():
        image_positions = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(img_matrix)):
            for j in range(len(img_matrix[i])):
                if img_matrix[i][j] != 'x':
                    pos = (j*100+5, i*100+5)
                    WIN.blit(img_matrix[i][j], pos)
                    image_positions[i][j] = (img_matrix[i][j], pos[0], pos[1], 100, 100)
                else:
                    # Desenha um quadrado preto de 100x100
                    pos = (j*100+5, i*100+5)
                    pygame.draw.rect(WIN, (0, 0, 0), (pos[0], pos[1], 100, 100))
                    image_positions[i][j] = ('x', pos[0], pos[1], 100, 100)

        return image_positions

    def move_img(img):
        for i in range(len(img_matrix)):
            for j in range(len(img_matrix[i])):
                if img_matrix[i][j] == img:
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

    # Função para lidar com eventos de clique do mouse
    def handle_click(image_positions):
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(image_positions)):
            for j in range(len(image_positions[i])):
                if is_point_in_rect(mouse_pos, (image_positions[i][j][1], image_positions[i][j][2], 100, 100)):
                    move_img(image_positions[i][j][0])
                    return  # Adiciona um return para sair da função após detectar um clique

    img_matrix = scramble_matrix(img_matrix)  # Embaralha a matriz antes do início do jogo

    while run:
        clock.tick(60)  # Ajusta a taxa de atualização para 60 FPS
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Detecta cliques do mouse
                handle_click(image_positions)
        
        image_positions = draw_images()
        pygame.display.update()  # Atualiza a tela após desenhar as imagens

main_game()