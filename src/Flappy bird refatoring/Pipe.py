import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale2x(pygame.image.load('assets/images/pipe/pipe-green.png').convert_alpha())