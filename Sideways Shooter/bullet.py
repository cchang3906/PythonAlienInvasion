import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create bullet at (0, 0) and move position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        #store bullet position
        self.x = float(self.rect.x)

    def update(self):
        """update bullet position"""

        #update bullet position
        self.x += self.settings.bullet_speed
        #update rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
