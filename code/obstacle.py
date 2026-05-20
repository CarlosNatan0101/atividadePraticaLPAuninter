import random
import pygame

from code.const import WIN_WIDTH


class Obstacle:

    def __init__(self):

        # =========================
        # OBSTÁCULOS
        # =========================

        self.obstacles_data = [

            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        './asset/obsPedra.png'
                    ).convert_alpha(),
                    (70, 70)
                ),

                "y": 390,

                "hitbox": (10, 10, 45, 45)
            },

            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        './asset/obsRaiz.png'
                    ).convert_alpha(),
                    (70, 70)
                ),

                "y": 390,

                "hitbox": (10, 10, 45, 45)
            },

            {
                "image": pygame.transform.scale(
                    pygame.image.load(
                        './asset/obsTronco.png'
                    ).convert_alpha(),
                    (90, 50)
                ),

                "y": 420,

                "hitbox": (10, 10, 70, 30)
            }
        ]

        # =========================
        # ESCOLHER PRIMEIRO
        # =========================

        current = random.choice(self.obstacles_data)

        self.image = current["image"]

        self.y = current["y"]

        self.hitbox = current["hitbox"]

        # =========================
        # POSIÇÃO
        # =========================

        self.x = WIN_WIDTH + 200

        # =========================
        # VELOCIDADE
        # =========================

        self.speed = 6

        # =========================
        # HITBOX
        # =========================

        self.rect = pygame.Rect(

            self.x + self.hitbox[0],

            self.y + self.hitbox[1],

            self.hitbox[2],

            self.hitbox[3]
        )

    def move(self, move_speed):

        # =========================
        # MOVIMENTO
        # =========================

        self.x -= move_speed

        # =========================
        # ATUALIZAR HITBOX
        # =========================

        self.rect.x = self.x + self.hitbox[0]

        self.rect.y = self.y + self.hitbox[1]

        # =========================
        # RESETAR OBSTÁCULO
        # =========================

        if self.x < -150:

            self.x = WIN_WIDTH + random.randint(200, 500)

            # novo obstáculo
            current = random.choice(self.obstacles_data)

            self.image = current["image"]

            self.y = current["y"]

            self.hitbox = current["hitbox"]

            # atualizar tamanho hitbox
            self.rect.width = self.hitbox[2]

            self.rect.height = self.hitbox[3]

    def draw(self, window):

        # desenhar obstacle
        window.blit(self.image, (self.x, self.y))
