import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from invader import Invader
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:

	def __init__(self):
		pygame.init()

		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption(self.settings.caption)

		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.invaders = pygame.sprite.Group()

		self._create_fleet()

		self.play_button = Button(self, 'Play')

	def run_game(self):
		while True:
			self._check_events()			
			self.ship.update()
			self._update_bullets()
			self._update_invader()
			self._update_screen()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
			elif event.type == pygame.KEYDOWN:
				self._check_KEYDOWN(event)		
			
			elif event.type == pygame.KEYUP:
				self._check_KEYUP(event)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)


	def _check_KEYDOWN(self,event):
		if event.key == pygame.K_RIGHT:
			self.ship.move_R = True
		
		elif event.key == pygame.K_LEFT:
			self.ship.move_L = True
		
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

		elif event.key == pygame.K_q:
			sys.exit()

		elif event.key == pygame.K_r:
			self.stats.reset_stats()
			self.stats.game_active = True

	def _check_KEYUP(self,event):
			if event.key == pygame.K_RIGHT:
				self.ship.move_R = False
			
			elif event.key == pygame.K_LEFT:
				self.ship.move_L = False

	def _check_fleet_edges(self):
		for invader in self.invaders.sprites():
			if invader.check_edges():
				self._change_fleet_direction()
				break
	
	def _check_play_button(self, mouse_pos):
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)

		if button_clicked and not self.stats.game_active:
			self.settings.initialize_dynamic_settings()
			self.stats.reset_stats()
			self.stats.game_active = True			
			self.invaders.empty()
			self.bullets.empty()
			self._create_fleet()
			self.ship.center_ship()

			pygame.mouse.set_visible(False)

	def _change_fleet_direction(self):
		for invader in self.invaders.sprites():
			invader.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _check_bullet_invader_collision(self):
		collisions = pygame.sprite.groupcollide(self.bullets, self.invaders, False, True)
		if collisions:
			self.stats.score += self.settings.invader_points
			self.sb.prep_score()

		if not self.invaders:
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()

	def _check_aliens_bottom(self):
		screen_rect = self.screen.get_rect()		
		for invader in self.invaders.sprites():
			if invader.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break

	def _update_screen(self):
		
		if not self.stats.game_active:
			self.screen.blit(self.settings.bg_scaled,(0, 0))
			self.play_button.draw_button()
			self.sb.show_score()

		else:	
			self.screen.blit(self.settings.bg_scaled,(0, 0))
			self.ship.blitship()

			for bullet in self.bullets.sprites():
				bullet.draw_bullet()

			self.invaders.draw(self.screen)

			self.sb.show_score()


		pygame.display.flip()

	def _update_bullets(self):
		self.bullets.update()

		for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)

		self._check_bullet_invader_collision()
	
	def _update_invader(self):
		self._check_fleet_edges()
		self.invaders.update()

		if pygame.sprite.spritecollideany(self.ship, self.invaders):
			self._ship_hit()

		self._check_aliens_bottom()

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _create_fleet(self):
		#Create the fleet of Invaders
		invader = Invader(self)
		invader_width, invader_height = invader.rect.size
		#How many alien on one row
		available_space_x = self.settings.screen_width - (2 * invader_width)
		number_invader_x = available_space_x // (2 * invader_width)
		#How many Rows
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * invader_height) - ship_height)
		number_rows = available_space_y // (2 * invader_height)

		#Create Full Fleet
		for row_num in range(number_rows):
			for invader_num in range(number_invader_x):	
				self._create_invader(invader_num, row_num)

	def _create_invader(self, invader_num, row_num):
		invader = Invader(self)
		invader_width, invader_height = invader.rect.size
		invader.x = invader_width + (2 * invader_width * invader_num)
		invader.rect.x = invader.x
		invader.rect.y = invader.rect.height + (2 * invader_height * row_num)
		self.invaders.add(invader)

	def _ship_hit(self):
		self.stats.ships_left -= 1
		
		if self.stats.ships_left == 0:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

		self.invaders.empty()
		self.bullets.empty()

		self._create_fleet()
		self.ship.center_ship()

		sleep(0.5)

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()