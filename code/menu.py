import pygame

from code.const import WIN_WIDTH


class Menu:
    def __init__(self, window):

        self.window = window

        self.image = pygame.image.load('./asset/bcgmenu.png')
        self.rect = self.image.get_rect()


        self.title_font = pygame.font.SysFont('Arial', 50, bold=True)
        self.text_font = pygame.font.SysFont('Arial', 18)


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


        pygame.mixer.music.load('./asset/natureambientsound.wav')
        pygame.mixer.music.play(-1)

    def run(self):

        self.window.blit(self.image, self.rect)

        self.window.blit(self.title, (20, 15))

        self.window.blit(self.text, (70, 220))