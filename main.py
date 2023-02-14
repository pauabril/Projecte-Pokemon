import pygame
from pygame.locals import *
import sys
from game_state import GlobalGameState

from config import *

from game import Game
from menu import Menu

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Pokemon")
pygame.display.set_icon(pygame.image.load(LOGO))

clock = pygame.time.Clock()

game = Game(screen)
# game.setup()

menu = Menu(screen, game)
menu.setup()

while game.global_gamestate != GlobalGameState.ENDED:
	clock.tick(60)

	match game.global_gamestate:
		case GlobalGameState.NONE:
			menu.update()
		case GlobalGameState.RUNNING:
			game.update()

	pygame.display.update()
