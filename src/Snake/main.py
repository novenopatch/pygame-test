import sys, pygame,random

class Snake:
    def __init__(self):
        self.UP = "up"
        self.DOWN = "down"
        self.RIGHT = "right"
        self.LEFT = "left"
        self.body = [pygame.math.Vector2(5,10),pygame.math.Vector2(6,10),pygame.math.Vector2(7,10)]
        self.direction =  pygame.math.Vector2(1,0)
        self.newBlock = False

    def drawSnake(self):
        for block in self.body:
            posX = int(block.x * cellSize)
            posY = int(block.y * cellSize)
            blockRect = pygame.Rect(posX,posY,cellSize,cellSize)
            pygame.draw.rect(screen, (183, 111, 122), blockRect)
    def moveSnake(self):
        if self.newBlock == True:
            bodyCopy = self.body[:]
            bodyCopy.insert(0, bodyCopy[0] + self.direction)
            self.body = bodyCopy[:]
            self.newBlock = False
        else:
            bodyCopy = self.body[:-1]
            bodyCopy.insert(0,bodyCopy[0] + self.direction)
            self.body = bodyCopy[:]

    def adBlock(self):
        self.newBlock = True
    def changeDirection(self,direction:str):
        if direction == self.UP:
            self.direction = pygame.math.Vector2(0, -1)
        if direction == self.DOWN:
            self.direction = pygame.math.Vector2(0, 1)
        if direction == self.RIGHT:
            self.direction = pygame.math.Vector2(1, 0)
        if direction == self.LEFT:
            self.direction = pygame.math.Vector2(-1, 0)

class Fruit:
    def __init__(self):
        self.randomize()
    def randomize(self):
        self.x = random.randint(0, cellNumber - 1)
        self.y = random.randint(0, cellNumber - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)
    def drawFruit(self):
        #create rectable
        fruitRect = pygame.Rect(int(self.pos.x * cellSize),int(self.pos.y * cellSize),cellSize,cellSize)
        pygame.draw.rect(screen,(126,166,144),fruitRect)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    def update(self):
        self.snake.moveSnake()
    def drawElements(self):
        self.snake.drawSnake()
        self.fruit.drawFruit()
    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.adBlock()
            #self.snake.moveSnake()

pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber * cellSize, cellNumber * cellSize))
clock = pygame.time.Clock()
running = True

mainGame = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
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
    screen.fill((175, 215, 70))
    mainGame.drawElements()
    mainGame.checkCollision()
    pygame.display.update()
    clock.tick(60)
