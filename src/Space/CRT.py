from random import randint

import pygame


class CRT:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.tv = pygame.image.load('assets/images/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (self.screen_width, self.screen_height))

    def create_crt_lines(self):
        line_height = 3
        line_amount = int(self.screen_height / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0, y_pos), (self.screen_width, y_pos), 1)

    def draw(self):
        self.tv.set_alpha(randint(79, 90))
        self.create_crt_lines()
        self.screen.blit(self.tv, (0, 0))
