import pygame

import config

from game_state import GlobalGameState, RunningGameState


class Battle:
	def __init__(self, screen, pokemon, player):
		self.screen = screen
		self.pokemon = pokemon
		self.pokemonimg = pygame.image.load(config.POKEMON_SPRITE['totodile']).convert_alpha() # REMOVE
		self.player = player

	def load(self):
		pass

	def render(self):
		self.screen.fill(config.WHITE)

		rect = pygame.Rect(1, 1, 2, 2)
		# self.screen.blit(self.pokemon.img, rect)
		self.screen.blit(self.pokemonimg, rect)
	
	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pass
