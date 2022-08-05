import pygame

class SoundManager:
    def __init__(self):
        self.sounds ={
            'eat': 'assets/sounds/crunch.wav',
        }
    def play(self,name):
        self.sounds[name].play()