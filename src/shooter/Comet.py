import pygame
import random
from Monster import Mummy, Alien


class Comet(pygame.sprite.Sprite):
    def __init__(self, cometEvent):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.cometEvent = cometEvent

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 500:
            self.remove()
            if len(self.cometEvent.allComets) == 0:
                self.cometEvent.resetPercent()
                self.cometEvent.fallMode = False
        if self.cometEvent.game.checkCollison(self, self.cometEvent.game.allPlayers):
            self.remove()
            self.cometEvent.game.player.damage(20)

    def remove(self):
        self.cometEvent.allComets.remove(self)
        # v nbr comm
        if len(self.cometEvent.allComets) == 0:
            self.cometEvent.resetPercent()
            self.cometEvent.game.start()
