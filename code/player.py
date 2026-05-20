import pygame


class Player:

    def __init__(self):

        self.frames = [

            pygame.transform.scale(
                pygame.image.load(
                    './asset/galinha1r.png'
                ).convert_alpha(),
                (90, 90)
            ),

            pygame.transform.scale(
                pygame.image.load(
                    './asset/galinha2r.png'
                ).convert_alpha(),
                (90, 90)
            ),

            pygame.transform.scale(
                pygame.image.load(
                    './asset/galinha3r.png'
                ).convert_alpha(),
                (90, 90)
            )
        ]

        self.current_frame = 0

        self.animation_speed = 0.15

        self.image = self.frames[self.current_frame]

        self.x = 500
        self.y = 360

        self.rect = pygame.Rect(
            self.x + 20,
            self.y + 15,
            50,
            60
        )

        self.speed = 0.3

        self.velocity_y = 0

        self.gravity = 0.8

        self.jump_force = -15

        self.ground_y = 360

        self.on_ground = True

    def animate(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:

            self.current_frame += self.animation_speed

            if self.current_frame >= len(self.frames):

                self.current_frame = 0

            self.image = self.frames[int(self.current_frame)]

    def move(self):

        keys = pygame.key.get_pressed()

        #if keys[pygame.K_a]:
           # self.x -= self.speed

        if keys[pygame.K_d]:
            #self.x += self.speed
            pass

        # pulo
        if keys[pygame.K_SPACE] and self.on_ground:

            self.velocity_y = self.jump_force

            self.on_ground = False

        # gravidade
        self.velocity_y += self.gravity

        self.y += self.velocity_y

        # chão
        if self.y >= self.ground_y:

            self.y = self.ground_y

            self.velocity_y = 0

            self.on_ground = True

        # atualizar hitbox
        self.rect.x = self.x + 20
        self.rect.y = self.y + 15

    def draw(self, window):

        window.blit(self.image, (self.x, self.y))

        # pygame.draw.rect(window, (255,0,0), self.rect, 2)