import pygame


class Monster(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 950
        self.rect.y = 550
        self.velocity = 2

    def forward(self):
        if not self.game.checkCollison(self,self.game.allPlayers):
            self.rect.x -= self.velocity

