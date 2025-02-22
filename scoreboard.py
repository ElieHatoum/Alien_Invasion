import pygame.font

class Scoreboard:

	def __init__(self, ai):
		self.screen = ai.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai.settings
		self.stats = ai.stats

		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		self.prep_score()

	def prep_score(self):
		self.score_str = str(self.stats.score)
		self.score_image = self.font.render(self.score_str, True,
		self.text_color)
		#Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)

