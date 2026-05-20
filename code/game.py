import sys
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.level import Level
from code.menu import Menu


class Jogo:

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        pygame.display.set_caption("Chicken Rush")


        pygame.mixer.music.load('./asset/natureambientsound.wav')

        pygame.mixer.music.play(-1)


        self.clock = pygame.time.Clock()

        self.menu = Menu(self.window)

        self.level = Level(self.window)

        self.state = "MENU"

    def run(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()


                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    # ENTER
                    if event.key == pygame.K_RETURN:


                        if self.state == "MENU":

                            # música gameplay
                            pygame.mixer.music.load('./asset/gameplayMusic.mp3')

                            pygame.mixer.music.play(-1)

                            self.level = Level(self.window)

                            self.state = "LEVEL"

                        elif self.state == "GAME_OVER":

                            pygame.mixer.music.load(
                                './asset/gameplayMusic.mp3'
                            )

                            pygame.mixer.music.play(-1)

                            self.level = Level(self.window)

                            self.state = "LEVEL"

                        elif self.state == "WIN":

                            pygame.mixer.music.load(
                                './asset/gameplayMusic.mp3'
                            )

                            pygame.mixer.music.play(-1)

                            self.level = Level(self.window)

                            self.state = "LEVEL"

                    if event.key == pygame.K_ESCAPE:

                        pygame.quit()

                        sys.exit()

            if self.state == "MENU":

                self.menu.run()

            elif self.state == "LEVEL":

                result = self.level.run()

                if result == "GAME_OVER":

                    # voltar música menu
                    pygame.mixer.music.load('./asset/natureambientsound.wav')

                    pygame.mixer.music.play(-1)

                    self.state = "GAME_OVER"


                if result == "WIN":

                    # voltar música menu
                    pygame.mixer.music.load( './asset/natureambientsound.wav')

                    pygame.mixer.music.play(-1)

                    self.state = "WIN"

            elif self.state == "GAME_OVER":

                self.window.fill((0, 0, 0))

                font1 = pygame.font.SysFont(
                    'Arial',
                    60,
                    bold=True
                )

                font2 = pygame.font.SysFont(
                    'Arial',
                    28
                )

                text1 = font1.render(
                    'GAME OVER',
                    True,
                    (255, 0, 0)
                )

                text2 = font2.render(
                    'ENTER = reiniciar | ESC = sair',
                    True,
                    (255, 255, 255)
                )

                self.window.blit(text1, (250, 180))

                self.window.blit(text2, (180, 300))

            elif self.state == "WIN":

                self.window.fill((20, 20, 20))

                font1 = pygame.font.SysFont(
                    'Arial',
                    60,
                    bold=True
                )

                font2 = pygame.font.SysFont(
                    'Arial',
                    28
                )

                text1 = font1.render(
                    'VOCE VENCEU!',
                    True,
                    (0, 255, 0)
                )

                text2 = font2.render(
                    'ENTER = jogar novamente | ESC = sair',
                    True,
                    (255, 255, 255)
                )

                self.window.blit(text1, (220, 180))

                self.window.blit(text2, (150, 300))

            pygame.display.flip()

            self.clock.tick(60)