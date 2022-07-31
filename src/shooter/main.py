import pygame
from Game import Game

pygame.init()
screenT = (1080, 720)

# make root
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode(screenT)
background = pygame.image.load('assets/bg.jpg')
# create game
game = Game()
running = True
# gui loop

while running:
    # get event loop
    screen.blit(background, (0, -200))

    screen.blit(game.player.image, game.player.rect)
    for projectile in game.player.allProjectiles:
        projectile.move()
    for monster in game.allMonsters:
        monster.forward()
    game.allMonsters.draw(screen)
    game.player.allProjectiles.draw(screen)
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width() :
        game.player.move("right")
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move("left")

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
