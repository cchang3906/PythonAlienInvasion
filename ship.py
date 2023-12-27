import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """class to manage the ship"""

    def __init__(self, ai_game):
        """initialize ship and starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        #movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """draw ship image at location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the ship's location based on flags"""
        if self.moving_right:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
        if self.moving_left:
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        """center the ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)