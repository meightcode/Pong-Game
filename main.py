import pygame, sys
from constants import *
from game import *

game = Game()

while True :
	clock.tick(clock_tick)
	for event in pygame.event.get():

		if event.type == pygame.QUIT :
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN :
			if event.key == pygame.K_z:
				game.moveUp(0)
			elif event.key == pygame.K_s:
				game.moveDown(0)
			elif event.key == pygame.K_UP:
				game.moveUp(1)
			elif event.key == pygame.K_DOWN:
				game.moveDown(1)
			elif event.key == pygame.K_KP_MINUS:
				clock_tick -= 3
			elif event.key == pygame.K_KP_PLUS:
				clock_tick += 3
			elif event.key == pygame.K_LEFT:
				game.changeMode(True)
			elif event.key == pygame.K_RIGHT:
				game.changeMode(False)
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_z:
				game.stopMoveUp(0)
			elif event.key == pygame.K_s:
				game.stopMoveDown(0)
			elif event.key == pygame.K_UP:
				game.stopMoveUp(1)
			elif event.key == pygame.K_DOWN:
				game.stopMoveDown(1)

	game.update()
	game.draw()


	pygame.display.flip()
	screen.fill([235,235,235])