import pygame
import config
import random

from player import Player
from game_state import GameState

import time # NOTE: only for testing start screen

class Menu:
	def __init__(self, screen, game):
		self.screen = screen
		self.game = game # TODO: Better way to do this

	def setup(self):
		self.menu_img = pygame.image.load(config.BG["start"])

	def update(self):
		self.screen.fill(config.BLACK)
		self.screen.blit(self.menu_img, (0,0))
		self.handle_events()

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.game.game_state = GameState.ENDED

			# ─── Handle Key Events ────────────────────────────────
			elif event.type == pygame.KEYDOWN:
				match event.key:
					case pygame.K_ESCAPE:
						self.game.game_state = GameState.ENDED
					case pygame.K_RETURN:
						self.game.setup()
						self.game.game_state = GameState.RUNNING
