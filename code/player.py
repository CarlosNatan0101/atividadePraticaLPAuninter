import pygame


class Player:

    def __init__(self):

        # imagem
        self.image = pygame.image.load(
            './asset/galinha1r.png'
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (90, 90)
        )

        # posição
        self.x = 360
        self.y = 360

        # movimento
        self.speed = 0.05

        # gravidade
        self.velocity_y = 0
        self.gravity = 0.8

        # pulo
        self.jump_force = -15

        # chão
        self.ground_y = 360

        # controle
        self.on_ground = True

    def move(self):

        keys = pygame.key.get_pressed()

        # =========================
        # MOVIMENTO HORIZONTAL
        # =========================

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

        # =========================
        # PULO
        # =========================

        if keys[pygame.K_SPACE] and self.on_ground:

            self.velocity_y = self.jump_force
            self.on_ground = False

        # =========================
        # GRAVIDADE
        # =========================

        self.velocity_y += self.gravity

        self.y += self.velocity_y

        # =========================
        # CHÃO
        # =========================

        if self.y >= self.ground_y:

            self.y = self.ground_y

            self.velocity_y = 0

            self.on_ground = True

    def draw(self, window):

        window.blit(
            self.image,
            (self.x, self.y)
        )