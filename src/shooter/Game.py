from Player import Player
from Monster import Monster
import pygame


class Game:
    def __init__(self):
        self.allPlayers = pygame.sprite.Group()
        self.player = Player(self)
        self.allPlayers.add(self.player)
        self.pressed = {}
        self.allMonsters = pygame.sprite.Group()
        self.spawnMonster()
        self.spawnMonster()

    def spawnMonster(self):
        monster = Monster(self)
        self.allMonsters.add(monster)

    def checkCollison(self, sprite, group):

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
