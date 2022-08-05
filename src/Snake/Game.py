import pygame
from Snake import Snake
from Fruit import Fruit
from Sounds import SoundManager
class Game:
    def __init__(self,cellNumber,cellSize):
        self.cellNumber = cellNumber
        self.cellSize = cellSize
        self.snake = Snake(self.cellSize)
        self.fruit = Fruit(self.cellNumber,self.cellSize)
        self.soundManager = SoundManager()
        self.gameFont = pygame.font.SysFont("monospace", 25)


    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkFail()

    def drawElements(self,screen):
        self.drawGrass(screen)

        self.snake.drawSnake(screen)
        self.fruit.drawFruit(screen)
        self.drawScore(screen)

    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.soundManager.play('eat')
            self.fruit.randomize()
            self.snake.adBlock()
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
    def drawGrass(self,screen):
        grassColor = (167,209,61)
        for row in range(self.cellNumber):
            if row % 2 ==0:
                for col in range(self.cellNumber):
                    if col % 2 == 0 :
                        grassRect = pygame.Rect(col * self.cellNumber,row * self.cellNumber,self.cellNumber,self.cellNumber)
                        pygame.draw.rect(screen,grassColor,grassRect)
            else:
                for col in range(self.cellNumber):
                    if col % 2 != 0 :
                        grassRect = pygame.Rect(col * self.cellSize,row * self.cellSize,self.cellSize,self.cellSize)
                        pygame.draw.rect(screen,grassColor,grassRect)
    def drawScore(self,screen):
        scoreText = str(len(self.snake.body) -3)
        scoreSurface = self.gameFont.render(scoreText,True,(56,74,12))
        scoreX = int(self.cellSize * self.cellNumber - 60)
        scoreY = int(self.cellSize * self.cellNumber - 40)
        scoreRect = scoreSurface.get_rect(center = (scoreX,scoreY))
        fruitRect = self.fruit.image.get_rect(midright=(scoreRect.left,scoreRect.centery))
        bgRect = pygame.Rect(fruitRect.left,fruitRect.top,fruitRect.width + scoreRect.width +7,fruitRect.height)

        pygame.draw.rect(screen,(167,209,61),bgRect)
        screen.blit(scoreSurface, scoreRect)
        screen.blit(self.fruit.image,fruitRect)
        pygame.draw.rect(screen,(56,74,12),bgRect,2)
