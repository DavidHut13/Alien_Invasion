class GameStats:
    """Track all stats for the game"""
    def __init__(self,ai_game):
        """Initialize Stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state
        self.game_active = False

    def reset_stats(self):
        """reset stats after game."""
        self.ships_left = self.settings.ship_limit

    