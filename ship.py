import pygame

class Ship:
    """ This class handles all the settings for the players ship"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.rect.midbottom = self.screen_rect.midbottom
        
    def track_ship_movement(self):
        if self.moving_right and self.rect.x < self.screen_rect.right - 65:
            self.x +=  self.settings.ship_speed
        if self.moving_left and self.rect.x > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.y > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.y < self.screen_rect.bottom - 54:
            self.y += self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y
        # print("x:{} y:{} top:{}".format(self.rect.x,self.rect.y,self.screen_rect.right))

    

    def blitme(self):
        self.screen.blit(self.image,self.rect)