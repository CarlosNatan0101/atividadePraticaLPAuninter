import pygame


class Fox:

    def __init__(self):

        self.frames = [

            pygame.transform.scale(
                pygame.image.load(
                    './asset/raposa1r.png'
                ).convert_alpha(),
                (140, 140)
            ),

            pygame.transform.scale(
                pygame.image.load(
                    './asset/raposa2r.png'
                ).convert_alpha(),
                (140, 140)
            )
        ]

        self.current_frame = 0

        self.animation_speed = 0.10

        self.image = self.frames[self.current_frame]

        self.x = -120
        self.y = 340

        self.speed = 0.1

        self.rect = pygame.Rect(
            self.x + 25,
            self.y + 30,
            70,
            80
        )

    def animate(self):

        self.current_frame += self.animation_speed

        if self.current_frame >= len(self.frames):

            self.current_frame = 0

        self.image = self.frames[int(self.current_frame)]

    def move(self):

        self.x += self.speed

        self.rect.topleft = (self.x, self.y)

        # atualizar hitbox
        self.rect.x = self.x + 25
        self.rect.y = self.y + 30

    def draw(self, window):

        window.blit(self.image, (self.x, self.y))

        # pygame.draw.rect(window, (255, 0, 0), self.rect, 2)