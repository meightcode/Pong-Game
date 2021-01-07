import pygame

win = [1080,720]

clock = pygame.time.Clock()
screen = pygame.display.set_mode((win[0],win[1]))
title = pygame.display.set_caption("RoundGame")
white = [(1,1,1)]
pygame.init()


clock_tick = 140
font = pygame.font.Font(None, 30)