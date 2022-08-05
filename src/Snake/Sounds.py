import pygame

class SoundManager:
    def __init__(self):
        self.sounds ={
            'eat': pygame.mixer.Sound('assets/sounds/crunch.wav'),
        }
    def play(self,name):
        self.sounds[name].play()