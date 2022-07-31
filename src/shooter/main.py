import pygame
from Game import Game
import math

pygame.init()
screenT = (1080, 720)

# make root
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode(screenT)
background = pygame.image.load('assets/bg.jpg')

banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner,(500,500))
bannerRect = banner.get_rect()
bannerRect.x = math.ceil(screen.get_width() / 4)

playButton = pygame.image.load("assets/button.png")
playButton = pygame.transform.scale(playButton,(400,150))
playButtonRect = playButton.get_rect()
playButtonRect.x = math.ceil(screen.get_width() / 3.33)
playButtonRect.y = math.ceil(screen.get_height() / 2)
# create game
game = Game()
running = True
# gui loop

while running:
    # get event loop
    screen.blit(background, (0, -200))

    if game.isPlaying:
        game.update(screen)
    else:

        screen.blit(playButton,playButtonRect)
        screen.blit(banner, bannerRect)

    #print(game.player.rect.x)
    # refresh screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launchProjectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if playButtonRect.collidepoint(event.pos):
                game.start()

