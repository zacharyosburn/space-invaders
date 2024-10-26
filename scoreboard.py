import pygame.font

class Scoreboard:
    """A class to represent scoring information"""
    def __init__(self, ai_game):
        """Initialize scoring attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font for the scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont (None, 48)
        # Prepares the initial scoring image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Make scoreboard a rendered image on screen"""
        score = self.stats.score
        score_str = f"{score:,}"
        self.score_image = self.font.render(score_str,
                True, self.text_color, self.settings.bg_color)
        
        # Display at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Make High Score visible on screen"""
        high_score = self.stats.high_score
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str,
                True, self.text_color, self.settings.bg_color)
        
        # Place High score at top center of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Checks for new high scores"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draws score images on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)