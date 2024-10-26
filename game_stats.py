class GameStats:
    """Track game stats for Alien Invasion Game"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset (just updated)
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that are updated during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        