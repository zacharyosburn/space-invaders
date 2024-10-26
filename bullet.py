from typing import Any
import pygame
from pygame.sprite import Group, Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Creates bullet at the ship's current destination"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                    self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Storing the bullet position as a float on y axis
        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet up the screen"""
        # Update the exact bullet position (Since y coordinate decreases as you move up screen, you use -= instead of +=)
        self.y -= self.settings.bullet_speed
        # Update the position of the rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)