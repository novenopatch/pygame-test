import sys, pygame, random


class Snake:
    def __init__(self):
        self.UP = "up"
        self.DOWN = "down"
        self.RIGHT = "right"
        self.LEFT = "left"
        self.body = [pygame.math.Vector2(5, 10), pygame.math.Vector2(4, 10), pygame.math.Vector2(3, 10)]
        self.direction = pygame.math.Vector2(1, 0)
        self.newBlock = False

        self.headUp = pygame.transform.scale(pygame.image.load('assets/head_up.png').convert_alpha(),
                                             (int(cellSize), int(cellSize)))
        self.headDown = pygame.transform.scale(pygame.image.load('assets/head_down.png').convert_alpha(),
                                               (int(cellSize), int(cellSize)))
        self.headRight = pygame.transform.scale(pygame.image.load('assets/head_right.png').convert_alpha(),
                                                (int(cellSize), int(cellSize)))
        self.headLeft = pygame.transform.scale(pygame.image.load('assets/head_left.png').convert_alpha(),
                                               (int(cellSize), int(cellSize)))

        self.tailUp = pygame.transform.scale(pygame.image.load("assets/tail_up.png").convert_alpha(),
                                             (int(cellSize), int(cellSize)))
        self.tailDown = pygame.transform.scale(pygame.image.load("assets/tail_down.png").convert_alpha(),
                                               (int(cellSize), int(cellSize)))
        self.tailRight = pygame.transform.scale(pygame.image.load("assets/tail_right.png").convert_alpha(),
                                                (int(cellSize), int(cellSize)))
        self.tailLeft = pygame.transform.scale(pygame.image.load("assets/tail_left.png").convert_alpha(),
                                               (int(cellSize), int(cellSize)))

        self.bodyVertical = pygame.transform.scale(pygame.image.load("assets/body_vertical.png").convert_alpha(),
                                                   (int(cellSize), int(cellSize)))
        self.bodyHorizontal = pygame.transform.scale(pygame.image.load("assets/body_horizontal.png").convert_alpha(),
                                                     (int(cellSize), int(cellSize)))

        self.bodyUp = pygame.transform.scale(pygame.image.load("assets/body_up.png").convert_alpha(),
                                             (int(cellSize), int(cellSize)))
        self.bodyDown = pygame.transform.scale(pygame.image.load("assets/body_down.png").convert_alpha(),
                                               (int(cellSize), int(cellSize)))
        self.bodyRight = pygame.transform.scale(pygame.image.load("assets/body_right.png").convert_alpha(),
                                                (int(cellSize), int(cellSize)))
        self.bodyLeft = pygame.transform.scale(pygame.image.load("assets/body_left.png").convert_alpha(),
                                               (int(cellSize), int(cellSize)))

    def drawSnake(self):
        # for block in self.body:
        #    posX = int(block.x * cellSize)
        #    posY = int(block.y * cellSize)
        #    blockRect = pygame.Rect(posX,posY,cellSize,cellSize)
        #    pygame.draw.rect(screen, (183, 111, 122), blockRect)
        for index, block in enumerate(self.body):
            posX = int(block.x * cellSize)
            posY = int(block.y * cellSize)
            blockRect = pygame.Rect(posX, posY, cellSize, cellSize)
            if index == 0:
                screen.blit(self.headRight, blockRect)
            else:
                pygame.draw.rect(screen, (150, 100, 100), blockRect)

    def moveSnake(self):
        if self.newBlock == True:
            bodyCopy = self.body[:]
            bodyCopy.insert(0, bodyCopy[0] + self.direction)
            self.body = bodyCopy[:]
            self.newBlock = False
        else:
            bodyCopy = self.body[:-1]
            bodyCopy.insert(0, bodyCopy[0] + self.direction)
            self.body = bodyCopy[:]

    def adBlock(self):
        self.newBlock = True

    def changeDirection(self, direction: str):
        if direction == self.UP:
            self.direction = pygame.math.Vector2(0, -1)
            if self.direction.y != 1:
                self.direction = pygame.math.Vector2(0, -1)
        if direction == self.DOWN:
            self.direction = pygame.math.Vector2(0, 1)
            if self.direction.y != -1:
                self.direction = pygame.math.Vector2(0, 1)
        if direction == self.RIGHT:
            self.direction = pygame.math.Vector2(1, 0)
            if self.direction.x != -1:
                self.direction = pygame.math.Vector2(1, 0)
        if direction == self.LEFT:
            self.direction = pygame.math.Vector2(-1, 0)
            if self.direction.x != 1:
                self.direction = pygame.math.Vector2(-1, 0)


class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        # super().__init__()
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, cellNumber - 1)
        self.y = random.randint(0, cellNumber - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)

    def drawFruit(self):
        # create rectable
        fruitRect = pygame.Rect(int(self.pos.x * cellSize), int(self.pos.y * cellSize), cellSize, cellSize)
        screen.blit(fruit, fruitRect)
        # {random.randint(1,2)}
        # pygame.draw.rect(screen,(126,166,114),fruitRect)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkFail()

    def drawElements(self):
        self.snake.drawSnake()
        self.fruit.drawFruit()

    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.adBlock()

    def checkFail(self):
        if not 0 <= self.snake.body[0].x < cellNumber or not 0 <= self.snake.body[0].y < cellNumber:
            self.gameOver()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameOver()

    def gameOver(self):

        pygame.quit()
        sys.exit()


pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber * cellSize, cellNumber * cellSize))
clock = pygame.time.Clock()
fruit = pygame.image.load(f'assets/fruit{random.randint(1, 2)}.png').convert_alpha()
fruit = pygame.transform.scale(fruit, (int(cellSize), int(cellSize)))
running = True
mainGame = Main()

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
    mainGame.drawElements()
    pygame.display.update()
    clock.tick(60)
