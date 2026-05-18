import sys

import pygame

#criar tela
pygame.init()
window = pygame.display.set_mode((800, 600))

while True:
    #fechar programa ao clicar no x vermelho
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()