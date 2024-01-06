import pygame
from pygame.sprite import Sprite
from rocket_settings import Settings
from random import randint

class Alien(Sprite):
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.left = self.screen.get_rect().right
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)
        
        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        
    def update(self):
        """Move the alien down"""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x
        
            
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.top >= screen_rect.top) or (self.rect.bottom <= 0)