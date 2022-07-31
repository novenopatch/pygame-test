import pygame
import random


class Monster(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.attack = 0.3
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 950 + random.randint(0, 300)
        self.rect.y = 550
        self.velocity = random.randint(1, 4)
    def damage(self,amount:int):
        self.health -= amount
        if self.health <= 0:
            #le faire revivre
            self.rect.x = 950 + random.randint(0, 300)
            self.health = self.maxHealth
            self.velocity = random.randint(1, 4)
            if self.game.cometEvent.isFullLoaded():
                self.game.allMonsters.remove(self)
    def updateHeathBar(self,surface):

        #position barPosition= [x,y,w,h]

        #draw
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y -10, self.maxHealth, 5] )
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y -10, self.health, 5] )

    def forward(self):
        if not self.game.checkCollison(self, self.game.allPlayers):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

