import pygame

class SoundManager:

    def __init__(self):
        self.sounds ={
            "music": pygame.mixer.Sound("assets/sounds/music.wav"),
            "explosion": pygame.mixer.Sound("assets/sounds/explosion.wav"),
            "laser" : pygame.mixer.Sound("assets/sounds/laser.wav")
        }
    def play(self,name,volume=0.2,loops= 0):
        self.sounds[name].play(loops=loops)
        self.sounds[name].set_volume(volume)
