import pygame
import random
from Animation import AnimateSprite


class Monster(AnimateSprite):
    def __init__(self, game, name,size,offset=0):
        super().__init__(name,size)
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.startAnimation()

    def damage(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            # le faire revivre
            self.rect.x = 950 + random.randint(0, 300)
            self.health = self.maxHealth
            self.velocity = random.randint(1, self.defaultSpeed)
            if self.game.cometEvent.isFullLoaded():
                self.game.allMonsters.remove(self)
                self.game.cometEvent.attemptFall()

    def updateAnimation(self):
        self.animate(True)

    def updateHeathBar(self, surface):

        # position barPosition= [x,y,w,h]

        # draw
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 10, self.maxHealth, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 10, self.health, 5])

    def forward(self):
        if not self.game.checkCollison(self, self.game.allPlayers):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
    def setSpeed(self,speed):
        self.defaultSpeed = speed
        self.velocity = random.randint(1,self.defaultSpeed)


class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy",(130,130))
        self.setSpeed(3)


class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien",(300,300),130)
        self.health = 250
        self.maxHealth = 250
        self.attack = 0.8
        self.setSpeed(1)
