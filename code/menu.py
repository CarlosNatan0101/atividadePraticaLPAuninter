import sys

import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.image = pygame.image.load('./asset/bcgmenu.png')
        self.rect = self.image.get_rect()

    def run(self):


        pygame.mixer.music.load("./asset/natureambientsound.wav")
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(self.image, self.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
