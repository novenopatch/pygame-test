import pygame
from Projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.allProjectiles = pygame.sprite.Group()

    def damage(self, amount: int):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.gameOver()

    def updateHeathBar(self, surface):

        # position barPosition= [x,y,w,h]

        # draw
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.maxHealth, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def launchProjectile(self):
        self.allProjectiles.add(Projectile(self))

    def move(self, direction: str):
        if not self.game.checkCollison(self, self.game.allMonsters):
            if direction == "right":
                self.rect.x += self.velocity
        if direction == "left":
            self.rect.x -= self.velocity
