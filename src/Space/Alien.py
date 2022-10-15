import pygame
class Alien (pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        file_path = "assets/images/" + color + ".png"
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft =(x,y))
        if color == 'red':
            self.value = 300
            self.heath = 5
        elif color == 'green':
            self.value = 100
            self.heath = 1
        else:
            self.value = 100
            self.heath = 3


    def update(self,direction):
        self.rect.x += direction
    def update_health(self):
        self.heath -= 1
        if self.heath <= 0:
            self.kill()

class Extra  (pygame.sprite.Sprite):
    def __init__(self,side,screen_width):
        super().__init__()
        self.image = pygame.image.load("assets/images/extra.png").convert_alpha()
        if side == "right":
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3
        self.rect = self.image.get_rect(topleft =(x,80))
    def update(self):
        self.rect.x += self.speed

