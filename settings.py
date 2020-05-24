class Settings:
    """ Settings for the game. """
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (33, 33, 33)
        self.speedup_scale = 1.1
        self.score_scale = 1.5
         # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 4
        self.bullet_height = 25
        self.bullet_color = (0, 207, 255)

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right: -1 riepresents left
        self.fleet_direction = 1

        # Ship settings
        self.ship_limit = 3
        self.ship_speed = 2

        

    def initialize_dynamic_settings(self):
        """Initialize settings that change in game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
