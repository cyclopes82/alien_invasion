import sys

import pygame

from raindrops_settings import Settings
from raindrop import Raindrop
     


class Rains:
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
        pygame.display.set_caption("Rains")

        self.raindrops = pygame.sprite.Group()
        
        self._create_drops()
        
          
    def run_game(self):        
        """Start the main loop for the game"""
        while True:
            self._check_events()  
            self._update_raindrops()                 
            self._update_screen()
            self.clock.tick(60)
            
            
        
    def _check_events(self):
        """Responds to key presses and mouse events."""    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

                    
    def _check_keydown_event(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_q:
            sys.exit()
            

    def _update_raindrops(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.raindrops.update()

    def _create_drops(self):
        """Create the fleet of raindrrops."""
        #Create a raindrop and keep adding raindrops untill there's no room left.
        #Spacing between raindrops is one raindrop width
        rain = Raindrop(self)
        raindrop_width, raindrop_height = rain.rect.size    
        
        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.settings.screen_height - 3 * raindrop_height):
            while current_x < (self.settings.screen_width - 2 * raindrop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width
                
            current_x = raindrop_width
            current_y += 2 * raindrop_height
            
    def _create_raindrop(self, x_position, y_position):
        """Create an alien and place it in the row"""
        new_raindrop = Raindrop(self)
        new_raindrop.x = x_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)
        
    def _create_new_row(self):
        """Create a new row of raindrops after a row disappears."""
        # Note: There are a number of ways to do this. This approach just
        #   copies the code from _create_drops() that's used for a single
        #   row of raindrops. This is simpler than trying to make 
        #   _create_drops() handle the full screen of raindrops, or a single
        #   new row of raindrops.
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size

        current_x = drop_width
        current_y = -1 * drop_height
        while current_x < (self.settings.screen_width - 2 * drop_width):
            self._create_drop(current_x, current_y)
            current_x += 2 * drop_width
            
    def _update_raindrops(self):
        """Update drop positions, and look for drops
        that have disappeared.

        Note: This solution isn't perfect; there's some space between periods
          of rain. But it should give the idea of how to steadily create new
          rows of drops. You can adjust the spacing to get a more uniform rain
          effect, especially with smaller drops and randomized positions.
        """
        self.raindrops.update()

        # Assume we won't make new drops.
        make_new_drops = False
        for drop in self.raindrops.copy():
            if drop. ():
                # Remove this drop, and we'll need to make new drops.
                self.raindrops.remove(drop)
                make_new_drops = True

        # Make a new row of drops if needed.
        if make_new_drops:
            self._create_new_row()
        
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for raindrop in self.raindrops.sprites():
            if raindrop.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction.""" 
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += self.settings.raindrop_drop_speed
        self.settings.fleet_direction *= -1      
                                    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        # for bullet in self.bullets.sprites():
        #     bullet.draw_bullet()
        # self.ship.blitme()
        
        self.raindrops.draw(self.screen)
        
        pygame.display.flip()
 



if __name__ == '__main__':
    # Make a game instance, and run the game.
    raindrop_game = Rains()
    raindrop_game.run_game()
    

