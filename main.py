import pygame
from pygame.locals import *
import sys
from game_state import GameState

from config import *

from game import Game

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Pokemon")
pygame.display.set_icon(pygame.image.load(LOGO))

clock = pygame.time.Clock()

game = Game(screen)
game.setup()

while game.game_state == GameState.RUNNING:
	clock.tick(60)
	game.update()
	pygame.display.update()
