import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self, ai):
		#Create Bullet Object on Ships position

		super().__init__()
		self.screen = ai.screen
		self.settings = ai.settings
		self.color = self.settings.bullet_color


		#Create rectangle on (0, 0)
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai.ship.rect.midtop

		#Store Bullet position
		self.y = float(self.rect.y)

	def update(self):
		#Change Bullet coordinate
		self.y -= float(self.settings.bullet_speed)

		#Update Bullet position
		self.rect.y = self.y

	def draw_bullet(self):
		#Draw Bullet on the screen
		pygame.draw.rect(self.screen, self.color, self.rect)

	


		


