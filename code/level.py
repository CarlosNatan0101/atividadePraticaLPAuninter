import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player


class Level:

    def __init__(self, window):

        self.window = window

        # =========================
        # BACKGROUNDS
        # =========================

        bg1 = pygame.image.load('./asset/bcg1Nuvens.png').convert()
        bg2 = pygame.image.load('./asset/bcg2arv.png').convert_alpha()
        bg3 = pygame.image.load('./asset/bcg3arv.png').convert_alpha()
        bg4 = pygame.image.load('./asset/bcg4piso.png').convert_alpha()

        # escala imagens
        bg1 = pygame.transform.scale(bg1, (WIN_WIDTH, WIN_HEIGHT))
        bg2 = pygame.transform.scale(bg2, (WIN_WIDTH, WIN_HEIGHT))
        bg3 = pygame.transform.scale(bg3, (WIN_WIDTH, WIN_HEIGHT))
        bg4 = pygame.transform.scale(bg4, (WIN_WIDTH, WIN_HEIGHT))

        # layers
        self.layers = [

            [bg1, 0, bg1.get_width(), 1],

            [bg2, 0, bg2.get_width(), 2],

            [bg3, 0, bg3.get_width(), 4],

            [bg4, 0, bg4.get_width(), 6]
        ]

        # player
        self.player = Player()

    def run(self):

        keys = pygame.key.get_pressed()

        # =========================
        # MOVER CENÁRIO
        # =========================

        if keys[pygame.K_d]:

            for layer in self.layers:

                layer[1] -= layer[3]
                layer[2] -= layer[3]

        # =========================
        # LOOP INFINITO
        # =========================

        for layer in self.layers:

            image = layer[0]

            if layer[1] <= -image.get_width():
                layer[1] = layer[2] + image.get_width()

            if layer[2] <= -image.get_width():
                layer[2] = layer[1] + image.get_width()

        # =========================
        # DESENHAR BACKGROUNDS
        # =========================

        for layer in self.layers:

            image = layer[0]

            self.window.blit(image, (layer[1], 0))
            self.window.blit(image, (layer[2], 0))

        # =========================
        # PLAYER
        # =========================

        self.player.move()
        self.player.draw(self.window)