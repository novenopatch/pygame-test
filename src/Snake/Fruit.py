import random, pygame


class Fruit(pygame.sprite.Sprite):
    def __init__(self, cellNumber: int, cellSize: int):
        super().__init__()
        self.cellSize = cellSize
        self.cellNumber = cellNumber
        self.image = pygame.image.load(f'assets/image/fruit{random.randint(1, 3)}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(cellSize), int(cellSize)))
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, self.cellNumber - 1)
        self.y = random.randint(0, self.cellNumber - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)

    def drawFruit(self, screen):
        # create rectable
        fruitRect = pygame.Rect(int(self.pos.x * self.cellSize), int(self.pos.y * self.cellSize), self.cellSize,
                                self.cellSize)
        screen.blit(self.image, fruitRect)
        # {random.randint(1,2)}
        # pygame.draw.rect(screen,(126,166,114),fruitRect)
