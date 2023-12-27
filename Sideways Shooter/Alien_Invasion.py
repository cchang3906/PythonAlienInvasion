import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


class AlienInvasion:
	"""class for game assets and behavior"""

	def __init__(self):
		"""initialize game and resources"""
		pygame.init()
		self.settings  = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.stats = GameStats(self)
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def _create_fleet(self):
		"""creates fleet of aliens"""
		#create an alien and find the number of aliens in a row
		#spacing each alien equal to one alien width
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		#determine the number of rows of aliens that can fit on screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		#create fleet
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

		#add aliens
		alien = Alien(self)
		self.aliens.add(alien)

	def _create_alien(self, alien_number, row_number):
		"""create alien and place in row"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""responds if any aliens reached an edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""drop the entire fleet and change fleet direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed

		self.settings.fleet_direction *= -1

	def _check_keydown_events(self, event):
		"""responds to when key is pressed"""
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""responds to when key is not pressed"""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _check_events(self):
		"""responds to keyboard and mouse input"""
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

	def _fire_bullet(self):
		"""create bullet and add to group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_screen(self):
		"""updates the game screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		#self.aliens.draw(self.screen)

		pygame.display.flip()

	def _update_bullets(self):
		"""update position of bullets and delete olds"""
		#update bullet position
		self.bullets.update()

		#delete old bullets
		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.settings.screen_width:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

		if not self.aliens:
			#destroy existing bullets and create new fleet
			self.bullets.empty()
			self._create_fleet()

	def _check_bullet_alien_collisions(self):
		"""delete aliens that hit bullets"""
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

	def _update_aliens(self):
		"""update positions of aliens"""
		self._check_fleet_edges()
		self.aliens.update()
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		self._check_aliens_bottom()

	def _check_aliens_bottom(self):
		"""check if any aliens have reached the bottom of the screen"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				#same as if the ship got hit
				self._ship_hit()
				break

	def _ship_hit(self):
		"""respond to the ship being hit by an alien"""
		if self.stats.ships_left > 0:
			#subtract 1 hp
			self.stats.ships_left -= 1
			#reset
			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()
			#pause
			sleep(0.5)
		else:
			self.stats.game_active = False

	def run_game(self):
		"""runs the loop for the game"""
		while True:
			self._check_events()

			if self.stats.game_active == True:
				#self._update_aliens()
				self.ship.update()
				self._update_bullets()

			self._update_screen()


if __name__ == '__main__':
	#game instance, and running game
	ai = AlienInvasion()
	ai.run_game()