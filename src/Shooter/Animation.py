import pygame

import random
#
class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, spriteName:str,size=(200,200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{spriteName}.png')
        self.image = pygame.transform.scale(self.image,size)
        self.currentImage = 0
        self.images = animations.get(spriteName)
        self.animation = False

    def startAnimation(self):
        self.animation = True
    def animate(self,loop:bool=False):
        if self.animation:
            self.currentImage += random.randint(0,1)
            if self.currentImage >= len(self.images):
                self.currentImage = 0
                if not  loop:
                    self.animation = False
            self.image = self.images[self.currentImage]
            self.image = pygame.transform.scale(self.image, self.size)


#
def loadAnimationImages(spriteName):
    images = []
    path = f"assets/{spriteName}/{spriteName}"
    for num in range(1, 24):
        imagePath = path + str(num) + ".png"
        images.append(pygame.image.load(imagePath))
    return images

animations = {
    'mummy':loadAnimationImages('mummy'),
    'player':loadAnimationImages('player'),
    'alien':loadAnimationImages('alien')
}