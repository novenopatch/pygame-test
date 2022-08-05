import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self,cellSize):
        super().__init__()
        self.UP = "up"
        self.DOWN = "down"
        self.RIGHT = "right"
        self.LEFT = "left"
        self.reset()
        self.newBlock = False
        self.cellSize = cellSize

        self.headUp = pygame.transform.scale(pygame.image.load('assets/image/head/head_up.png').convert_alpha(),
                                             (int(cellSize) + 1, int(cellSize) + 1))
        self.headDown = pygame.transform.scale(pygame.image.load('assets/image/head/head_down.png').convert_alpha(),
                                               (int(cellSize), int(cellSize)))
        self.headRight = pygame.transform.scale(pygame.image.load('assets/image/head/head_right.png').convert_alpha(),
                                                (int(cellSize), int(cellSize)))
        self.headLeft = pygame.transform.scale(pygame.image.load('assets/image/head/head_left.png').convert_alpha(),
                                               (int(cellSize), int(cellSize)))

        self.tailUp = pygame.transform.scale(pygame.image.load("assets/image/tail/tail_up.png").convert_alpha(),
                                             (int(cellSize), int(cellSize)))
        self.tailDown = pygame.transform.scale(pygame.image.load("assets/image/tail/tail_down.png").convert_alpha(),
                                               (int(cellSize), int(cellSize)))
        self.tailRight = pygame.transform.scale(pygame.image.load("assets/image/tail/tail_right.png").convert_alpha(),
                                                (int(cellSize), int(cellSize)))
        self.tailLeft = pygame.transform.scale(pygame.image.load("assets/image/tail/tail_left.png").convert_alpha(),
                                               (int(cellSize), int(cellSize)))

        self.bodyVertical = pygame.transform.scale(pygame.image.load(
            "assets/image/body/body_vertical.png").convert_alpha(),
                                                   (int(cellSize), int(cellSize)))
        self.bodyHorizontal = pygame.transform.scale(pygame.image.load(
            "assets/image/body/body_horizontal.png").convert_alpha(),
                                                     (int(cellSize), int(cellSize)))

        self.bodyTopRight = pygame.transform.scale(pygame.image.load("assets/image/body/body_tr.png").convert_alpha(),
                                                   (int(cellSize) , int(cellSize)))
        self.bodyTopLeft = pygame.transform.scale(pygame.image.load("assets/image/body/body_tl.png").convert_alpha(),
                                                  (int(cellSize) , int(cellSize) ))
        self.bodyDownRight = pygame.transform.scale(pygame.image.load("assets/image/body/body_br.png").convert_alpha(),
                                                    (int(cellSize), int(cellSize)))
        self.bodyDownLeft = pygame.transform.scale(pygame.image.load("assets/image/body/body_bl.png").convert_alpha(),
                                                   (int(cellSize), int(cellSize)))

    def drawSnake(self,screen):
        self.updateHeadGraphics()
        self.updateTailGraphics()
        for index, block in enumerate(self.body):
            posX = int(block.x * self.cellSize)
            posY = int(block.y * self.cellSize)
            blockRect = pygame.Rect(posX, posY, self.cellSize, self.cellSize)
            if index == 0:
                screen.blit(self.head, blockRect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, blockRect)
            else:
                previousBlock = self.body[index + 1] - block
                nextBlock = self.body[index - 1] - block
                if previousBlock.x == nextBlock.x:
                    screen.blit(self.bodyVertical, blockRect)
                elif previousBlock.y == nextBlock.y:
                    screen.blit(self.bodyHorizontal, blockRect)
                else:
                    if previousBlock.x == -1 and nextBlock.y == -1 or previousBlock.y == -1 and nextBlock.x == -1:
                        screen.blit(self.bodyTopLeft, blockRect)
                    if previousBlock.x == -1 and nextBlock.y == 1 or previousBlock.y == 1 and nextBlock.x == -1:
                        screen.blit(self.bodyDownLeft, blockRect)
                    if previousBlock.x == 1 and nextBlock.y == -1 or previousBlock.y == -1 and nextBlock.x == 1:
                        screen.blit(self.bodyTopRight, blockRect)
                    if previousBlock.x == 1 and nextBlock.y == 1 or previousBlock.y == 1 and nextBlock.x == 1:
                        screen.blit(self.bodyDownRight, blockRect)

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
            #self.direction = pygame.math.Vector2(0, -1)
            if self.direction.y != 1:
                self.direction = pygame.math.Vector2(0, -1)
        if direction == self.DOWN:
            #self.direction = pygame.math.Vector2(0, 1)
            if self.direction.y != -1:
                self.direction = pygame.math.Vector2(0, 1)
        if direction == self.RIGHT:
            #self.direction = pygame.math.Vector2(1, 0)
            if self.direction.x != -1:
                self.direction = pygame.math.Vector2(1, 0)
        if direction == self.LEFT:
            #self.direction = pygame.math.Vector2(-1, 0)
            if self.direction.x != 1:
                self.direction = pygame.math.Vector2(-1, 0)

    def updateHeadGraphics(self):
        headRelation = self.body[1] - self.body[0]
        if headRelation == pygame.math.Vector2(1, 0):
            self.head = self.headLeft
        elif headRelation == pygame.math.Vector2(-1, 0):
            self.head = self.headRight
        elif headRelation == pygame.math.Vector2(0, 1):
            self.head = self.headUp
        elif headRelation == pygame.math.Vector2(0, -1):
            self.head = self.headDown

    def updateTailGraphics(self):
        tailRelation = self.body[-2] - self.body[-1]
        if tailRelation == pygame.math.Vector2(1, 0):
            self.tail = self.tailRight
        elif tailRelation == pygame.math.Vector2(-1, 0):
            self.tail = self.tailLeft
        elif tailRelation == pygame.math.Vector2(0, 1):
            self.tail = self.tailDown
        elif tailRelation == pygame.math.Vector2(0, -1):
            self.tail = self.tailUp

    def reset(self):
        self.body = [pygame.math.Vector2(5, 10), pygame.math.Vector2(4, 10), pygame.math.Vector2(3, 10)]
        self.direction = pygame.math.Vector2(0, 0)