import sys
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Jogo:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Chicken Rush")

        self.menu = Menu(self.window)

    def run(self):

        while True:

            for event in pygame.event.get():

                # fechar jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # apertar ENTER
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print("Jogo iniciado")

            # desenhar menu
            self.menu.run()

            pygame.display.flip()