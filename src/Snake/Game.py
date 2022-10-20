import sys
from Sounds import SoundManager
from Snake import Snake
from Fruit import Fruit
import pygame


class Game:
    def __init__(self,screen, cellNumber: int, cellSize: int):
        self.screen = screen
        self.cellNumber = cellNumber
        self.cellSize = cellSize
        self.snake = Snake(self.cellSize)
        self.fruit = Fruit(self.cellNumber, self.cellSize)
        self.gameFont = pygame.font.SysFont("monospace", 25)
        self.soundManager = SoundManager()

    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkFail()

    def drawElements(self):
        self.drawGrass()
        self.drawScore()
        self.snake.drawSnake(self.screen)
        self.fruit.drawFruit(self.screen)

    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.adBlock()
            self.soundManager.play('eat')
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def checkFail(self):
        if not 0 <= self.snake.body[0].x < self.cellNumber or not 0 <= self.snake.body[0].y < self.cellNumber:
            self.gameOver()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameOver()

    def gameOver(self):
        self.snake.reset()

    def drawGrass(self):
        grassColor = (167, 209, 61)
        for row in range(self.cellNumber):
            if row % 2 == 0:
                for col in range(self.cellNumber):
                    if col % 2 == 0:
                        grassRect = pygame.Rect(col * self.cellSize, row * self.cellSize, self.cellSize, self.cellSize)
                        pygame.draw.rect(self.screen, grassColor, grassRect)
            else:
                for col in range(self.cellNumber):
                    if col % 2 != 0:
                        grassRect = pygame.Rect(col * self.cellSize, row * self.cellSize, self.cellSize, self.cellSize)
                        pygame.draw.rect(self.screen, grassColor, grassRect)

    def drawScore(self):
        scoreText = str(len(self.snake.body) - 3)
        scoreSurface = self.gameFont.render(scoreText, True, (56, 74, 12))
        scoreX = int(self.cellSize * self.cellNumber - 60)
        scoreY = int(self.cellSize * self.cellNumber - 40)

        scoreRect = scoreSurface.get_rect(center=(scoreX, scoreY))
        fruitRect = self.fruit.image.get_rect(midright=(scoreRect.left, scoreRect.centery))
        bgRect = pygame.Rect(fruitRect.left, fruitRect.top, fruitRect.width + scoreRect.width + 6,
                             fruitRect.height)

        pygame.draw.rect(self.screen, (167, 209, 61), bgRect)
        self.screen.blit(scoreSurface, scoreRect)
        self.screen.blit(self.fruit.image, fruitRect)
        pygame.draw.rect(self.screen, (56, 74, 12), bgRect, 2)
