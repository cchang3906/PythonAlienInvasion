import pygame.font

class Button:

	def __init__(self, ai_game, msg):
		"""initialize button attributes"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		#set dimensions and properties of button
		self.width, self.height = 200, 50
		self.button_color = (0, 150, 100)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		#build button rect and center
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		#button as one time event
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""turn message into rendered image and center it"""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""drawing button"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)