import pygame
import sys

from CRT import CRT
from Game import Game

if __name__ == '__main__':

    pygame.init()
    screen_width = 600
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game(screen)
    crt = CRT(screen)

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game.alien_shoot()
        screen.fill((20, 30, 30))
        game.run()
        crt.draw()

        pygame.display.flip()
        clock.tick(90)
