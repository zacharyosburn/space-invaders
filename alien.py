import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent single alien on the screen"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image on screen and set the rect attribute
        self.image = pygame.image.load('images/alien_1.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing the exact hortizontal float of the alien
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Moves aliens to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x