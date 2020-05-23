class Settings:
    """ Settings for the game. """
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (33, 33, 33)
        
         # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 207, 255)

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right: -1 riepresents left
        self.fleet_direction = 1

        # Ship settings
        self.ship_limit = 3
        self.ship_speed = 2