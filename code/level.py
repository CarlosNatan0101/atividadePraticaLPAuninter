import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player
from code.obstacle import Obstacle
from code.fox import Fox


class Level:

    def __init__(self, window):

        self.window = window

        self.distance = 0

        self.font = pygame.font.SysFont(
            'Arial',
            28,
            bold=True
        )

        self.show_intro = True

        self.intro_timer = 300

        bg1 = pygame.image.load('./asset/bcg1Nuvens.png').convert()
        bg2 = pygame.image.load('./asset/bcg2arv.png').convert_alpha()
        bg3 = pygame.image.load('./asset/bcg3arv.png').convert_alpha()
        bg4 = pygame.image.load('./asset/bcg4piso.png').convert_alpha()

        # escala imagens
        bg1 = pygame.transform.scale(bg1, (WIN_WIDTH, WIN_HEIGHT))
        bg2 = pygame.transform.scale(bg2, (WIN_WIDTH, WIN_HEIGHT))
        bg3 = pygame.transform.scale(bg3, (WIN_WIDTH, WIN_HEIGHT))
        bg4 = pygame.transform.scale(bg4, (WIN_WIDTH, WIN_HEIGHT))

        # layers parallax
        self.layers = [

            [bg1, 0, bg1.get_width(), 1],

            [bg2, 0, bg2.get_width(), 2],

            [bg3, 0, bg3.get_width(), 4],

            [bg4, 0, bg4.get_width(), 6]
        ]

        self.barn = pygame.image.load(
            './asset/celeiro.png'
        ).convert_alpha()

        self.barn = pygame.transform.scale(
            self.barn,
            (400, 250)
        )

        self.barn_x = 25000
        self.barn_y = 220

        self.barn_rect = pygame.Rect(
            self.barn_x + 40,
            self.barn_y + 40,
            150,
            150
        )

        self.player = Player()

        self.obstacle = Obstacle()


        self.fox = Fox()

    def run(self):

        if self.show_intro:

            self.intro_timer -= 1

            if self.intro_timer <= 0:

                self.show_intro = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:

            self.distance += 1

            # mover celeiro
            self.barn_x -= 6

            # mover backgrounds
            for layer in self.layers:

                layer[1] -= layer[3]
                layer[2] -= layer[3]

            # mover obstacle
            self.obstacle.move(6)


        self.barn_rect.x = self.barn_x + 40


        for layer in self.layers:

            image = layer[0]

            if layer[1] <= -image.get_width():

                layer[1] = layer[2] + image.get_width()

            if layer[2] <= -image.get_width():

                layer[2] = layer[1] + image.get_width()

        for layer in self.layers:

            image = layer[0]

            self.window.blit(image, (layer[1], 0))
            self.window.blit(image, (layer[2], 0))

        self.window.blit(
            self.barn,
            (self.barn_x, self.barn_y)
        )

        self.player.move()
        self.player.animate()
        self.player.draw(self.window)

        self.obstacle.draw(self.window)

        self.fox.move()
        self.fox.animate()
        self.fox.draw(self.window)

        if self.show_intro:

            text1 = self.font.render(
                'Chegue ao celeiro antes que a raposa o alcance!',
                True,
                (255, 255, 255)
            )

            text2 = self.font.render(
                'D = correr | ESPACO = pular',
                True,
                (255, 255, 0)
            )

            self.window.blit(text1, (110, 80))

            self.window.blit(text2, (240, 130))

        # obstacle
        if self.player.rect.colliderect(
                self.obstacle.rect
        ):

            return "GAME_OVER"

        # fox
        if self.player.rect.colliderect(
                self.fox.rect
        ):

            return "GAME_OVER"

        # vitória
        if self.player.rect.colliderect(
                self.barn_rect
        ):

            return "WIN"