import sys, pygame, random

from Game import Game

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber * cellSize, cellNumber * cellSize))
clock = pygame.time.Clock()
running = True
mainGame = Game(cellNumber,cellSize)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            mainGame.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mainGame.snake.changeDirection(mainGame.snake.UP)
            if event.key == pygame.K_DOWN:
                mainGame.snake.changeDirection(mainGame.snake.DOWN)
            if event.key == pygame.K_LEFT:
                mainGame.snake.changeDirection(mainGame.snake.LEFT)
            if event.key == pygame.K_RIGHT:
                mainGame.snake.changeDirection(mainGame.snake.RIGHT)
    screen.fill((215, 215, 70))
    mainGame.drawElements(screen)
    pygame.display.update()
    clock.tick(60)
