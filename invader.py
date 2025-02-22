import pygame

from pygame.sprite import Sprite

class Invader(Sprite):

	def __init__(self, ai):
		super().__init__()
		self.screen = ai.screen
		self.settings = ai.settings

		#Load Invader Image
		self.image = pygame.image.load('Images/invader3.png')
		self.rect = self.image.get_rect()

		#Start Near Top Left
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store Invader exact Horiz position
		self.x = float(self.rect.x)

	def update(self):
		#Move Invader to the Right
		self.x += (self.settings.invader_speed * self.settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		screen_rect = self.screen.get_rect()

		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True


