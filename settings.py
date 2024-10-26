
class Settings:
    """Class being made to store all settings for the game"""

    def __init__(self):
        """Initialize the game settings"""
        # Screen Settings
        self.screen_width = 1440
        self.screen_height = 1080
        # Colors are (R, G, B)
        self.bg_color = (144, 144, 144)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (144, 0, 159)
        self.bullets_allowed = 5

        #Alien settings
        self.fleet_drop_speed = 10
        
        # Rate of speed increase in game
        self.speedup_scale = 1.2
        self.score_scale = 1.55

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings that change the longer the game goes"""
        self.ship_speed = 2
        self.bullet_speed = 3
        self.alien_speed = 1
        # fleet_direction of 1 represents rightward movement; -1 represnts leftward on the x-axis
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 51

    def increase_speed(self):
        """Increases speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)