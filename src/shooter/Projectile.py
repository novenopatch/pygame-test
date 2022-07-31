import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 150
        self.rect.y = player.rect.y + 80
        self.player = player
        self.originImage = self.image
        self.angle = 0

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        if self.player.game.checkCollison(self, self.player.game.allMonsters):
            self.remove()
        if self.rect.x > 1080:
            self.remove()

    def remove(self):
        self.player.allProjectiles.remove()

    def rotate(self):
        # vitesse de rotation
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.originImage, self.angle, 1)
        # pour avoir une rotation par rapport au centre
        self.rect = self.image.get_rect(center=self.rect.center)
