import pygame
from config import *

class Player:
	def __init__(self, pos_x, pos_y, snum="000", name="Player"):
		self.pos = (pos_x, pos_y)
		self.snum = snum
		self.sprite = pygame.image.load(PLAYER_SPRITE[snum + "down"])
		self.sprite = pygame.transform.scale(self.sprite, (SCALE, SCALE))
		self.rect = pygame.Rect(self.pos[0] * SCALE, self.pos[1] * SCALE, SCALE, SCALE)
		self.direction = "down"
		self.name = name
		print("Player created")

	def update(self):
		print("Player update")

	def update_pos(self, new_pos, direction):
		if self.direction != direction:
			self.update_direction(direction)
		else:
			self.pos = (new_pos[0], new_pos[1])
#			print("Player pos updated")

		# self.update_sprite(direction)
		# self.pos = (new_pos[0], new_pos[1])

	def update_direction(self, direction):
		if self.direction != direction:
			self.direction = direction
			self.sprite = pygame.image.load(PLAYER_SPRITE[self.snum + direction])
			self.sprite = pygame.transform.scale(self.sprite, (SCALE, SCALE))
#			print("Player direction updated")
		else:
			# self.pos = (new_pos[0], new_pos[1])
			print("can't update player pos (blocked)")
		

	def render(self, screen, cam):
		self.rect = pygame.Rect(self.pos[0] * SCALE - (cam[0] * SCALE), self.pos[1] * SCALE - (cam[1] * SCALE), SCALE, SCALE)
		screen.blit(self.sprite, self.rect)
