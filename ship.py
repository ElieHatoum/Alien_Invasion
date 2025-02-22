import pygame

class Ship:

	def __init__(self, ai):

		self.screen = ai.screen
		self.settings = ai.settings
		
		self.screen_rect = ai.screen.get_rect()

		#Load ship
		self.ship = pygame.image.load('Images/ship')
		self.rect = self.ship.get_rect()
		#Load ship at the bottom
		self.rect.midbottom = self.screen_rect.midbottom

		#Ship Movement
		self.x = float(self.rect.x)
		
		self.move_R = False
		self.move_L = False

	def update(self):
		if self.move_R and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed

		elif self.move_L == True and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		self.rect.x = self.x

	def blitship(self):
		self.screen.blit(self.ship, self.rect)

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)