import pygame
import config
import random

from player import Player
from game_state import GlobalGameState

class PauseMenu:
	def __init__(self, screen, game):
		self.screen = screen
		self.game = game # TODO: Better way to do this

	def setup(self):
		self.menu_bg = pygame.image.load(config.BG["start"])
		self.menu_bg = pygame.transform.scale(self.menu_bg, config.SCREEN_SIZE)

		self.menu_options_bg = pygame.Rect(config.SCREEN_SIZE[0] - 210, 10, 200, 280)		
		self.menu_options_border = pygame.Rect(config.SCREEN_SIZE[0] - 210+3, 10+3, 200-6, 280-6)		

		self.menu_options = [
			"Resume",
			"Save",
			"Inventory",
			"Pokemon",
			"Map",
			"Options",
			"Quit"
		]

		self.menu_selection = 0
		self.menu_selection_rect = pygame.Rect(config.SCREEN_SIZE[0] - 210+3, 10+3, 200-6, 40-6)

		for i in range(len(self.menu_options)):
			self.menu_options[i] = pygame.font.Font(config.FONT["pokemon"], 20).render(self.menu_options[i], True, config.BLACK)


	def update(self):
		# self.screen.fill(config.BLACK)
		# self.screen.blit(self.menu_bg, (0,0))

		pygame.draw.rect(self.screen, config.WHITE, self.menu_options_bg, 0, 2)
		pygame.draw.rect(self.screen, config.BLACK, self.menu_options_border, 3, 2)

		self.render_selection(config.WHITE)

		for i in range(len(self.menu_options)):
			# self.screen.blit(self.menu_options[i], (config.SCREEN_SIZE[0] / 2 - self.menu_options[i].get_width() / 2, 100 + i * 40)) # Centered
			self.screen.blit(self.menu_options[i], (config.SCREEN_SIZE[0] - self.menu_options[i].get_width() - 20, 20 + i * 40)) # Right Top

		self.handle_events()


	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.game.global_gamestate = GlobalGameState.ENDED

			# ─── Handle Key Events ────────────────────────────────
			elif event.type == pygame.KEYDOWN:
				match event.key:
					case pygame.K_ESCAPE: # Quit
						self.game.global_gamestate = GlobalGameState.ENDED
					case pygame.K_TAB | pygame.K_q: # Close menu
						self.game.global_gamestate = GlobalGameState.RUNNING
						self.menu_selection = 0
					case pygame.K_w | pygame.K_UP: # Move menu selection up
						self.move_selection(-1)
						print(self.menu_selection)
						pass
					case pygame.K_s | pygame.K_DOWN: # Move menu selection down
						self.move_selection(1)
						print(self.menu_selection)
						pass
					case pygame.K_e | pygame.K_RETURN: # Execute menu selection
						self.execute_selection()
						pass

	def move_selection(self, direction):
		if self.menu_selection + direction < 0:
			self.menu_selection = len(self.menu_options) - 1
		elif self.menu_selection + direction > len(self.menu_options) - 1:
			self.menu_selection = 0
		else:
			self.menu_selection += direction

		# self.render_selection(self.menu_selection)

	def render_selection(self, color=config.GRAY):
		pygame.draw.rect(self.screen, color, self.menu_selection_rect, 0)
		self.menu_selection_rect = pygame.Rect(config.SCREEN_SIZE[0] - 210+3, 10+3 + self.menu_selection * 40, 200-6, 40-6)
		pygame.draw.rect(self.screen, color, self.menu_selection_rect, 0)

	def execute_selection(self):
		match self.menu_selection:
			case 0: # Resume
				print("Resume")
				self.game.global_gamestate = GlobalGameState.RUNNING
				self.menu_selection = 0
			case 1: # Save
				print("Save")
				pass
			case 2: # Inventory
				print("Inventory")
				pass
			case 3: # Pokemon
				print("Pokemon")
				pass
			case 4: # Map
				print("Map")
				pass
			case 5: # Options
				print("Options")
				pass
			case 6: # Quit
				print("Quit")
				self.game.global_gamestate = GlobalGameState.ENDED
