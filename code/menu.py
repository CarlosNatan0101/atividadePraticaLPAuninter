import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT


class Menu:

    def __init__(self, window):

        self.window = window

        # imagem menu
        self.image = pygame.image.load('./asset/bcgmenu.png')

        self.image = pygame.transform.scale(
            self.image,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        self.rect = self.image.get_rect()

        # fontes
        self.title_font = pygame.font.SysFont(
            'Arial',
            75,
            bold=True
        )

        self.text_font = pygame.font.SysFont(
            'Arial',
            22
        )

        # textos
        self.title = self.title_font.render(
            'CHICKEN RUSH',
            True,
            (255, 140, 0)
        )

        self.text = self.text_font.render(
            'Pressione ENTER para jogar ou ESC para sair',
            True,
            (255, 255, 255)
        )

        # música
        pygame.mixer.music.load('./asset/natureambientsound.wav')
        pygame.mixer.music.play(-1)

    def run(self):

        self.window.blit(self.image, self.rect)

        self.window.blit(self.title, (20, 20))

        self.window.blit(self.text, (40, 400))