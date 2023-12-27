class Settings:
	"""class to store all settings"""

	def __init__(self):
		"""initualize static settings"""
		#Screen settings
		self.screen_width = 1700
		self.screen_height = 1000
		self.bg_color = (0, 0, 50)

		#Ship settings
		self.ship_speed = 10
		self.ship_limit = 2

		#Bullet settings
		self.bullet_speed = 10
		self.bullet_width = 10
		self.bullet_height = 100
		self.bullet_color = (230, 0, 0)
		self.bullets_allowed = 2

		#scoring settings
		self.alien_points = 500

		#alien settings
		self.alien_speed = 50
		self.fleet_drop_speed = 20
		#+1 represents right; -1 represents left
		self.fleet_direction = 1

		#speed up scale
		self.speedup_scale = 1.5
		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""initialize changable settings"""
		self.ship_speed = 6
		self.bullet_speed = 10
		self.alien_speed = 2
		self.score_scale = 2

		#score scale
		self.alien_points = int(self.alien_points * self.score_scale)

		#1 represents right; -1 represents left
		self.fleet_direction = 1

	def increase_speed(self):
		"""increase speed settings"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale