import sys, pygame, random
from Game import Game
from Direction import Direction

class Setup:
    def __init__(self):
        pygame.init()
        self.running = True
        self.cellSize = 40
        self.cellNumber = 20
        self.screen = pygame.display.set_mode((self.cellNumber * self.cellSize, self.cellNumber * self.cellSize))
        self.clock = pygame.time.Clock()
        self.game = Game(self.screen, self.cellNumber, self.cellSize)

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 150)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == self.SCREEN_UPDATE:
                    self.game.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.game.snake.changeDirection(Direction.UP)
                    if event.key == pygame.K_DOWN:
                        self.game.snake.changeDirection(Direction.DOWN)
                    if event.key == pygame.K_LEFT:
                        self.game.snake.changeDirection(Direction.LEFT)
                    if event.key == pygame.K_RIGHT:
                        self.game.snake.changeDirection(Direction.RIGHT)
            self.screen.fill((215, 215, 70))
            self.game.drawElements()
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    setup = Setup()
    setup.run()
