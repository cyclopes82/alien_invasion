import sys

import pygame

from settings import Settings
from ship import Ship
# from bird import Bird


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()        
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
        
          
    def run_game(self):
        
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
            
            
        
    def _check_events(self):
        """Responds to key presses and mouse events."""   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

                    
    def _check_keydown_event(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_event(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
                                        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()
 



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    
