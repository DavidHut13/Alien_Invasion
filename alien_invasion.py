import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet 

class AlienInvasion:
    """Return the sum of x and y."""
    def __init__(self):
        """ Class to manage game assests and behavior"""
        pygame.init()
        self.settings = Settings()
        # Full screen code below
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        # windowed code below
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()



    def _check_events(self):
        """ Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
                

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            #Move the ship to the right
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            #Move the ship to the right
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            #Move the ship to the right
            self.ship.moving_down = False

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            #Move the ship to the right
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            #Move the ship to the right
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            #Move the ship to the right
            self.ship.moving_down = True
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)  

   

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
        

    
    def run_game(self):
        """ Method handles running the game."""
        while True:
            self._check_events()
            self.ship.track_ship_movement()
            self._update_bullets()
            self._update_screen()

          
    
    def _update_bullets(self):
        """Update position of bullets and get rid of out of sight bullets"""
        # Update bullet position
        self.bullets.update()

        # Get rid of bullets that hae disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

                



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()