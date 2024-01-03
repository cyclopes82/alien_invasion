import pygame

class Bird:
    def __init__(self, ai_game) -> None:
        """Initialize the bird and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load("images/bird_small.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)