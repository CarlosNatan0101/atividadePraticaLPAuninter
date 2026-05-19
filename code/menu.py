import pygame


class Menu:
    def __init__(self, window):

        self.window = window

        self.image = pygame.image.load('./asset/bcgmenu.png')
        self.rect = self.image.get_rect()


        self.title_font = pygame.font.SysFont('Arial', 70, bold=True)
        self.text_font = pygame.font.SysFont('Arial', 30)


        self.title = self.title_font.render(
            'CHICKEN RUSH',
            True,
            (255, 255, 255)
        )

        self.text = self.text_font.render(
            'Pressione ENTER para jogar',
            True,
            (255, 255, 255)
        )


        pygame.mixer.music.load('./asset/natureambientsound.wav')
        pygame.mixer.music.play(-1)

    def run(self):

        # desenha fundo
        self.window.blit(self.image, self.rect)

        # desenha título
        self.window.blit(self.title, (170, 120))

        # desenha texto inferior
        self.window.blit(self.text, (200, 500))