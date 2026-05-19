import pygame


class Player:

    def __init__(self):

        # imagem
        self.image = pygame.image.load('./asset/galinha1.png')

        # posição
        self.x = 10
        self.y = 40

        # velocidade
        self.speed = 0.5

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, window):

        window.blit(self.image, (self.x, self.y))