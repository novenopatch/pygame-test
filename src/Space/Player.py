import pygame
from Laser import  Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen,speed:int,sound):
        super().__init__()

        self.screen = screen
        self.speed = speed
        self.image = pygame.image.load('assets/images/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.ready = True
        self.laser_time = 0
        self.laser_countdown = 600
        self.lasers = pygame.sprite.Group()
        self.soundManager = sound

    def get_input(self):

        #print(f"player x = {self.rect.x},player y = {self.rect.y} ")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x + self.rect.width < self.screen.get_width():
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_UP] and self.rect.y > 0:self.rect.y -= self.speed
        elif keys[pygame.K_DOWN] and self.rect.y + self.rect.height < self.screen.get_height():self.rect.y += self.speed
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_lase()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_countdown:
                self.ready = True
    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()

    def shoot_lase(self):
        self.lasers.add(Laser(self.rect.center,-8,self.rect.bottom))
        self.soundManager.play("laser",volume=0.5)