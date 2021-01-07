from constants import *
import math
import random

class Ball:
	def __init__(self):
		self.x = win[0]/2
		self.y = win[1]/2
		self.size = 30
		self.velocity = 4
		self.random = random.choice([(-45,45),(135,225)])
		print(self.random)
		self.angle = random.randint(self.random[0],self.random[1])
		self.image = pygame.transform.scale(pygame.image.load("img/ball.png"),(self.size,self.size))
		self.origin_image = self.image.copy()
		self.rect = self.image.get_rect()
	def move(self):
		self.x += math.cos(math.radians(self.angle))*self.velocity
		self.y += math.sin(math.radians(self.angle))*self.velocity
	def bounceVertical(self,translation,which_racquet):
		self.velocity = 8
		self.angle = 180-self.angle + translation*1
	def bounceHorizontal(self):
		self.angle = -self.angle
	def resetPosition(self):
		self.velocity = 4
		self.x = win[0]/2
		self.y = win[1]/2
		self.random = random.choice([(-45,45),(135,225)])
		self.angle = random.randint(self.random[0],self.random[1])
	def update(self):
		self.move()
		self.rect.x = self.x
		self.rect.y = self.y


