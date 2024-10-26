import pygame.font

class Button:
    """A class for on screen buttons in the game"""
    def __init__(self, ai_game, msg):
        """Initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Setting button dimensions and properties
        self.width, self.height = 270, 50
        self.button_color = (0, 0, 0)
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 45)

        # Build the button's rect obj, and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_message(msg)

    def _prep_message(self, msg):
        """Turn msg into image rendered on center of screen"""
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draws blank button, then draw msg"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)