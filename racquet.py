from constants import *

class Racquet:
	def __init__(self,position):
		self.moveup = False
		self.movedown = False
		self.velocity = 7
		self.image = pygame.image.load("img/racquet.png")
		self.y = win[1]//2 - self.image.get_height()//2
		if position :
			self.x = 60
		else :
			self.x = win[0]-60-self.image.get_width()
		self.rect = self.image.get_rect()
	def move(self):
		if self.moveup:
			self.y -= self.velocity
		elif self.movedown:
			self.y += self.velocity

	def update(self):
		self.rect.x = self.x
		self.rect.y = self.y
