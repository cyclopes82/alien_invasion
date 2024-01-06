import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
# from bird import Bird
from bullet import Bullet
from alien import Alien
from game_stat import GameStats     


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
       
        #Create an instance to store game statistics.
        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
         #Start Alien Invasion in an active state.
        self.game_active = True
        
        
          
    def run_game(self):
        
        """Start the main loop for the game"""
        while True:
            self._check_events()
            if self.game_active:
                
                self.ship.update()
                self._update_bullets()   
                self._update_aliens()                 
            
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_event(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()    
        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                #print(len(self.bullets))
        
        self._check_bullet_alien_collisons()
        
    def _check_bullet_alien_collisons(self):
        """Respond to bullet-alien collisions."""      
                
        #Check for any bullets that have hit aliens
        #If so, get rid of the bullent and the alien
        collsions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            #Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
                
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        
        #Look for alien-ship Collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        #Look for aliens hitting the bottom of the scrren
        self._check_aliens_bottom()
            
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        
        if (self.stats.ships_left > 0):
            
            #Decrement ships_left by 1        
            self.stats.ships_left -= 1
            #Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            
            #Create a new fleet and cetre the ship.
            self._create_fleet()
            self.ship.center_ship()
            
            #Pause.
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #Treat this the same way as if the ship got hit.
                self._ship_hit()
                break
    
    def _create_fleet(self):
        """Create the fleet of Aliens."""
        #Create an alien and keep adding aliens untill there's no room left.
        #Spacing between aliens is one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        

        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
                
            current_x = alien_width
            current_y += 2 * alien_height
            
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction.""" 
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1      
                                    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        
        self.aliens.draw(self.screen)
        
        pygame.display.flip()
 



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    

