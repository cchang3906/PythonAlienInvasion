class GameStats:
    """tracking stats"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        #game active state
        self.game_active = True

    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit