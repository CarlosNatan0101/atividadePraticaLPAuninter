import sys
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.level import Level
from code.menu import Menu


class Jogo:

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode(
            (WIN_WIDTH, WIN_HEIGHT)
        )

        pygame.display.set_caption("Chicken Rush")

        # FPS
        self.clock = pygame.time.Clock()

        # telas
        self.menu = Menu(self.window)
        self.level = Level(self.window)

        # estado atual
        self.state = "MENU"

    def run(self):

        while True:

            for event in pygame.event.get():

                # fechar
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # teclado
                if event.type == pygame.KEYDOWN:

                    # iniciar jogo
                    if event.key == pygame.K_RETURN:
                        self.state = "LEVEL"

                    # sair
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # menu
            if self.state == "MENU":
                self.menu.run()

            # level
            elif self.state == "LEVEL":
                self.level.run()

            pygame.display.flip()

            # FPS
            self.clock.tick(60)