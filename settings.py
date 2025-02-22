import pygame

class Settings:

	def __init__(self):

		#Screen Settings
		self.screen_width = 1100
		self.screen_height = 700
		self.caption = "Alien Invasion"

		#BackGround Settings
		self.bg = pygame.image.load('Images/bg1.jpg') 
		self.bg_scaled = pygame.transform.scale(self.bg,(1100, 700))

		#Ship Settings
		self.ship_speed = 2
		self.ship_limit = 3

		#Bullet Settings
		self.bullet_speed = 4
		self.bullet_width = 7
		self.bullet_height = 15
		self.bullet_color = (255, 0, 0)
		self.bullet_allowed = 10

		#Invader Settings
		self.invader_speed = 1
		#Fleet
		self.fleet_drop_speed = 1	
		#Fleet direction : Axis-X
		self.fleet_direction = 1

		self.speedup_scale = 1.1

	def initialize_dynamic_settings(self):

		self.ship_speed = 2
		self.bullet_speed = 2
		self.invader_speed = 1
		self.fleet_direction = 1
		self.invader_points = 10

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.invader_speed *= self.speedup_scale



