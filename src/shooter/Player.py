import pygame
from Projectile import  Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.allProjectiles = pygame.sprite.Group()

    def launchProjectile(self):
        self.allProjectiles.add(Projectile(self))
    def move(self, direction: str):
        if not self.game.checkCollison(self,self.game.allMonsters):
            if direction == "right":
                self.rect.x += self.velocity
        if direction == "left":
                self.rect.x -= self.velocity


