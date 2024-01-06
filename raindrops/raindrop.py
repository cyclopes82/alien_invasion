import pygame
from pygame.sprite import Sprite
from raindrops_settings import Settings


class Raindrop(Sprite):
    """A class to represent a single raindrop in the rain."""
    
    def __init__(self, raindrop_game):
        """Intialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = raindrop_game.screen
        self.settings = raindrop_game.settings
        
        #Load the raindrop image and set its rect attribute
      
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()
        
        #Start each new raindrop near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the raindrop's exact horizontal position
        self.x = float(self.rect.x)
        
    def update(self):
        """Move the raindrop to the right"""
        self.x += self.settings.raindrop_speed * self.settings.fleet_direction
        self.rect.x = self.x
        
    def check_edges(self):
        """Return True if raindrop is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def check_disappeared(self):
        """Check if drop has disappeared off bottom of screen."""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False