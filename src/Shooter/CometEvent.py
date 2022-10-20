import pygame
from Comet import  Comet

class CometFallEvent:
    def __init__(self,game):
        self.percent = 0
        self.percentSpeed = 10
        self.allComets = pygame.sprite.Group()
        self.game = game
        self.fallMode = False

    def meteorFall(self):
        for i in range(1,10):
            self.allComets.add(Comet(self))
    def addPercent(self):

        self.percent += self.percentSpeed / 100
    def isFullLoaded(self):
        return self.percent >= 100
    def resetPercent(self):
        self.percent = 0
    def attemptFall(self):
        if self.isFullLoaded() and len(self.game.allMonsters) == 0:
            self.meteorFall()
            #
            self.fallMode = True
    def updateBar(self, surface):
        self.addPercent()
        #
        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() -20,
            surface.get_width(),
            10
        ])
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() -20,
            (surface.get_width() /100) * self.percent,
            10
        ])




