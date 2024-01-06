import sys
from random import random

import pygame

from rocket_settings import Settings
from sideway_ship import Ship
from rocket_bullet import Bullet
from sideway_alien import Alien

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        # self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._create_alien()
            self.ship.update()
            self._update_bullets()
            self.aliens.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                 self.bullets.remove(bullet)
                 
        self._check_bullet_alien_collisons()
        
    def _check_bullet_alien_collisons(self):
        """Respond to bullet-alien collisions."""      
                
        #Check for any bullets that have hit aliens
        #If so, get rid of the bullent and the alien
        collsions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # if not self.aliens:
        #     #Destroy existing bullets and create new fleet.
        #     self.bullets.empty()
        #     self._create_fleet()
            
    def _create_alien(self):
        """Create an alien, if conditions are right."""
        if random() < self.settings.alien_frequency:
            alien = Alien(self)
            self.aliens.add(alien)
            
    # def _update_aliens(self):
    #     """Update the positions of all aliens in the fleet"""
    #     self._check_fleet_edges()
    #     self.aliens.update()
        
    # def _create_fleet(self):
    #     """Create the fleet of Aliens."""
    #     #Create an alien and keep adding aliens untill there's no room left.
    #     #Spacing between aliens is one alien width
    #     alien = Alien(self)
    #     alien_width, alien_height = alien.rect.size
    #     current_x, current_y = alien_width, alien_height
    #     while current_y < (self.settings.screen_height - 3 * alien_height):
    #         while current_x < (self.settings.screen_width - 2 * alien_width):
    #             self._create_alien(current_x, current_y)
    #             current_x += 2 * alien_width
                
    #         current_x = alien_width
    #         current_y += 2 * alien_height
            
            
    # def _create_alien(self, x_position, y_position):
    #     """Create an alien and place it in the row"""
    #     new_alien = Alien(self)
    #     new_alien.x = x_position
    #     new_alien.rect.x = x_position
    #     new_alien.rect.y = y_position
    #     self.aliens.add(new_alien)
        
    # def _check_fleet_edges(self):
    #     """Respond appropriately if any aliens have reached an edge."""
    #     for alien in self.aliens.sprites():
    #         if alien.check_edges():
    #             self._change_fleet_direction()
    #             break
    
    # def _change_fleet_direction(self):
    #     """Drop the entire fleet and change the fleet's direction.""" 
    #     for alien in self.aliens.sprites():
    #         alien.rect.y += self.settings.fleet_drop_speed
    #     self.settings.fleet_direction *= -1          


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss_game = SidewaysShooter()
    ss_game.run_game()