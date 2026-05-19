import pygame


class Player:

    def __init__(self):

        # imagem
        self.image = pygame.image.load('./asset/galinha1r.png').convert_alpha()

        # tamanho player
        self.image = pygame.transform.scale(self.image, (90, 90))

        # posição
        self.x = 100
        self.y = 360

        # velocidade
        self.speed = 1

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, window):

        window.blit(self.image, (self.x, self.y))