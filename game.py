from racquet import *
from ball import *
from constants import *
from random import randint
import pygame

class Game:
	def __init__(self):
		self.random = [0,0]
		self.repetition = 0
		self.mode = 0
		self.racquet = [Racquet(True),Racquet(False)]
		self.ball = Ball()
		self.score = [0,0]
		self.left_last_position_y = 0
		self.right_last_position_y = 0

	def moveUp(self,player):
		self.racquet[player].moveup = True

	def moveDown(self,player):
		self.racquet[player].movedown = True

	def stopMoveUp(self,player):
		self.racquet[player].moveup = False

	def stopMoveDown(self,player):
		self.racquet[player].movedown = False

	def checkCollide(self):
		if self.racquet[0].x < self.ball.x < self.racquet[0].x + self.racquet[0].image.get_width(): 
			if self.racquet[0].rect.y - self.ball.image.get_height()/2< self.ball.y + self.ball.image.get_height()/2 < self.racquet[0].rect.y + self.racquet[0].image.get_height()+ self.ball.image.get_height()/2:
				self.ball.bounceVertical(self.left_last_position_y-self.racquet[0].rect.y,True)

		elif self.racquet[1].x < self.ball.x + self.ball.image.get_width()< self.racquet[1].x + self.racquet[1].image.get_width(): 
			if self.racquet[1].rect.y - self.ball.image.get_height()/2 < self.ball.y + self.ball.image.get_height()/2 < self.racquet[1].rect.y + self.racquet[1].image.get_height()+ self.ball.image.get_height()/2:
				self.ball.bounceVertical(self.right_last_position_y-self.racquet[1].rect.y,False)

		elif self.racquet[0].x + self.racquet[0].image.get_width() + 1 < self.ball.x < self.racquet[0].x + self.racquet[0].image.get_width()*2:
			if self.racquet[0].rect.y - self.ball.image.get_height()/2< self.ball.y + self.ball.image.get_height()/2 < self.racquet[0].rect.y + self.racquet[0].image.get_height()+ self.ball.image.get_height()/2:
				self.left_last_position_y = self.racquet[0].rect.y
				self.right_last_position_y = 0

		elif self.racquet[1].x - self.racquet[1].image.get_width() -1 < self.ball.x + self.ball.image.get_width() < self.racquet[1].x:
			if self.racquet[1].rect.y - self.ball.image.get_height()/2 < self.ball.y + self.ball.image.get_height()/2 < self.racquet[1].rect.y + self.racquet[1].image.get_height()+ self.ball.image.get_height()/2:
				self.right_last_position_y = self.racquet[1].rect.y
				self.left_last_position_y = 0

		elif (self.ball.rect.center[1] < 0) or (self.ball.rect.center[1] > win[1]):
			self.ball.bounceHorizontal()

		elif self.ball.rect.center[0] < 0:
			self.restart(True)

		elif self.ball.rect.center[0] > win[0]:
			self.restart(False)

		if self.ball.rect.center[1] < -20 or self.ball.rect.center[1] > win[1]+20 or self.ball.rect.center[0]<-10 or self.ball.rect.center[0]>win[0]+10:
			if self.ball.rect.center[0] < win[0]/2:
				self.restart(True)
			else :
				self.restart(False)

		for i in range(2):
			if self.racquet[i].y < 0 and self.mode == 0:
				self.racquet[i].y += self.racquet[0].velocity
			elif self.racquet[i].y + self.racquet[i].image.get_height() > win[1] and self.mode == 0:
				self.racquet[i].y -= self.racquet[0].velocity

		if self.mode == 1 and self.racquet[0].y < 0 :
			self.racquet[0].y += self.racquet[0].velocity

		elif self.mode == 1 and self.racquet[0].y + self.racquet[0].image.get_height() > win[1] :
			self.racquet[0].y -= self.racquet[0].velocity

		if self.racquet[0].y < 0 and self.mode == 2:
			self.racquet[0].y += self.racquet[0].velocity

		elif self.racquet[0].y + self.racquet[0].image.get_height() > win[1] and self.mode == 2:
				self.racquet[0].y -= self.racquet[0].velocity



	def restart(self,winner):
		self.left_last_position_y = 0
		self.right_last_position_y = 0

		self.ball.resetPosition()
		if winner:
			self.score[0] = self.score[0]+1
		else :
			self.score[1] = self.score[1]+1
	def moveBOT(self,mode):
		if mode:
			if self.ball.x > win[0]//2:
				if self.ball.y < self.racquet[1].y + self.racquet[1].image.get_height()//2:
					self.racquet[1].y-=5
				else:
					self.racquet[1].y+=5
		else:
			if self.ball.x < win[0]//2:
				if self.ball.y < self.racquet[0].y + self.racquet[0].image.get_height()//2:
					if self.racquet[0].y > 0:
						self.racquet[0].y-=4
				else:
					if self.racquet[0].y + self.racquet[0].image.get_height() < win[1]:
						self.racquet[0].y+=4

			if self.ball.x > win[0]//3:
				if self.ball.y < self.racquet[1].y + self.racquet[1].image.get_height()//2:
					if self.racquet[1].y > 0:
						self.racquet[1].y-=4
				else:
					if self.racquet[1].y + self.racquet[1].image.get_height() < win[1]:
						self.racquet[1].y+=4

	def changeMode(self,left):
		self.score = [0,0]
		if left:
			if self.mode != 0:
				self.mode -= 1 
		elif self.mode != 2:
			self.mode += 1 

	def draw(self):
		for i in self.racquet:
			screen.blit(i.image, i.rect)
		pygame.draw.line(screen, ([0,0,0]), (win[0]/2,0), (win[0]/2,win[1]), 2)
		screen.blit(self.ball.image, self.ball.rect)

		self.score1_surface = font.render(str(self.score[1]), 1 , (0, 0, 0))
		self.score1_rect_surface = self.score1_surface.get_rect(center=(win[0]/2-self.score1_surface.get_width(), 5 + self.score1_surface.get_height()))
		screen.blit(self.score1_surface,(self.score1_rect_surface))

		self.score1_surface = font.render(str(self.score[0]), 1 , (0, 0, 0))
		self.score1_rect_surface = self.score1_surface.get_rect(center=(win[0]/2+self.score1_surface.get_width(), 5 + self.score1_surface.get_height()))
		screen.blit(self.score1_surface,(self.score1_rect_surface))

	def update(self):
		self.checkCollide()
		if self.mode == 1:
			self.racquet[0].move()
		for i in self.racquet:
			if self.mode == 0:
				i.move()
			elif self.mode == 1:
				self.moveBOT(True)
			else: 
				self.moveBOT(False)
			i.update()
		
		
		self.ball.update()


