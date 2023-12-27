import pygame
from settings import Settings
class Ship:
    """class to manage the ship"""

    def __init__(self, ai_game):
        """initialize ship and starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)
        #movement flag
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """draw ship image at location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the ship's location based on flags"""
        if self.moving_up:
            if self.moving_up and self.rect.top > 0:
                self.y -= self.settings.ship_speed
        if self.moving_down:
            if self.moving_down and self.rect.bottom < self.settings.screen_height:
                self.y += self.settings.ship_speed

        self.rect.y = self.y

    def center_ship(self):
        """center the ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)