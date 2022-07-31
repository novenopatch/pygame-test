from Player import Player
from Monster import Monster
from CometEvent import CometFallEvent
import pygame


class Game:
    def __init__(self):
        self.isPlaying = False
        #self.isPlaying = True
        self.allPlayers = pygame.sprite.Group()
        self.player = Player(self)
        self.allPlayers.add(self.player)
        self.pressed = {}
        self.allMonsters = pygame.sprite.Group()
        self.cometEvent = CometFallEvent(self)
    def start(self):
        self.isPlaying = True
        self.spawnMonster()
        self.spawnMonster()
    def gameOver(self):
        self.allMonsters = pygame.sprite.Group()
        self.player.health = self.player.maxHealth
        self.isPlaying = False
    def update(self,screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.updateHeathBar(screen)
        self.cometEvent.updateBar(screen)
        for projectile in self.player.allProjectiles:
            projectile.move()
        for monster in self.allMonsters:
            monster.forward()
            monster.updateHeathBar(screen)
        for comet in self.cometEvent.allComets:
            comet.fall()
        self.allMonsters.draw(screen)
        self.player.allProjectiles.draw(screen)
        self.cometEvent.allComets.draw(screen)
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move("right")
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move("left")
    def spawnMonster(self):
        monster = Monster(self)
        self.allMonsters.add(monster)

    def checkCollison(self, sprite, group):

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
