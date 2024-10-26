import pygame

class Ship:
    """Class to manage ship behaviors"""
    def __init__(self, ai_game):
        """Initialize ship and set starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start every ship at bottom middle of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement flag; start with ship that is not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag"""
        # Update ship's x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on bottom of screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)