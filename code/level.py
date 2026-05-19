import pygame

from code.player import Player


class Level:

    def __init__(self, window):

        self.window = window

        # backgrounds
        bg1 = pygame.image.load('./asset/bcg1Nuvens.png')
        bg2 = pygame.image.load('./asset/bcg2arv.png')
        bg3 = pygame.image.load('./asset/bcg3arv.png')
        bg4 = pygame.image.load('./asset/bcg4piso.png')

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

        # mover cenário
        if keys[pygame.K_d]:

            for layer in self.layers:

                layer[1] -= layer[3]
                layer[2] -= layer[3]

        # loop infinito
        for layer in self.layers:

            image = layer[0]

            if layer[1] <= -image.get_width():
                layer[1] = layer[2] + image.get_width()

            if layer[2] <= -image.get_width():
                layer[2] = layer[1] + image.get_width()

        # desenhar backgrounds
        for layer in self.layers:

            image = layer[0]

            self.window.blit(image, (layer[1], 0))
            self.window.blit(image, (layer[2], 0))

        # player
        self.player.move()
        self.player.draw(self.window)