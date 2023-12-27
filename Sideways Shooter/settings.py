class Settings:
	"""class to store all settings"""

	def __init__(self):
		#Screen settings
		self.screen_width = 1700
		self.screen_height = 1000
		self.bg_color = (0, 0, 50)

		#Ship settings
		self.ship_speed = 10
		self.ship_limit = 3

		#Bullet settings
		self.bullet_speed = 10
		self.bullet_width = 50
		self.bullet_height = 20
		self.bullet_color = (230, 0, 0)
		self.bullets_allowed = 3

		#alien settings
		self.alien_speed = 3
		self.fleet_drop_speed = 100
		#+1 represents right; -1 represents left
		self.fleet_direction = 1