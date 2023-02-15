import pygame
import random

from player import Player
from npc import Npc
from game_state import GlobalGameState, RunningGameState
from config import *
from game_view.map import Map

import time # NOTE: only for testing start screen

class Game:
	def __init__(self, screen):
		self.screen = screen
		self.objects = []
		self.global_gamestate = GlobalGameState.NONE
		self.running_gamestate = RunningGameState.MAP
		self.map = Map(screen)

	def setup(self):
		player = Player(1,1, snum="001") # TODO: move snum to user input
		self.player = player
		self.objects.append(player)

		self.map.load()

		npc1 = Npc(3, 3, name="npc1", snum="000") #TODO: make npcs talk and be linked to the map
		npc2 = Npc(4, 6, name="npc2", snum="003", direction="left")
		npc3 = Npc(0, 19, name="npc3", snum="001", direction="right",)
		self.objects.append(npc1)
		self.objects.append(npc2)
		self.objects.append(npc3)

		talking1 = Npc(17, 9, name="t1", snum="002", direction="down") #TODO
		talking2 = Npc(17, 10, name="t2",snum="001", direction="up") #TODO
		self.objects.append(talking1)
		self.objects.append(talking2)

		self.global_gamestate = GlobalGameState.RUNNING
		print("Setup")
					

	def update(self):
		match self.running_gamestate:
			case RunningGameState.MAP:
				self.screen.fill(BLACK)

				self.handle_events()

				self.map.render(self.screen, self.player, self.objects)
			
			case RunningGameState.BATTLE:
				pass

		# print("Update")

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.global_gamestate = GlobalGameState.ENDED

			# ─── Handle Key Events ────────────────────────────────
			elif event.type == pygame.KEYDOWN:
				match event.key:
					case pygame.K_ESCAPE | pygame.K_TAB: # menu
						self.global_gamestate = GlobalGameState.PAUSED
					case pygame.K_w | pygame.K_UP: # up
						self.move_unit(self.player, [0, -1], "up")
					case pygame.K_s | pygame.K_DOWN: # down
						self.move_unit(self.player, [0, 1], "down")
					case pygame.K_a | pygame.K_LEFT: # left
						self.move_unit(self.player, [-1, 0], "left")
					case pygame.K_d | pygame.K_RIGHT: # right
						self.move_unit(self.player, [1, 0], "right")
					case pygame.K_e: # interact
						self.interact()
					case _:
						pass


	def move_unit(self, unit, pos_change, direction):
		new_pos = [unit.pos[0] + pos_change[0], unit.pos[1] + pos_change[1]]

		if new_pos[0] < 0 or new_pos[0] >= (len(self.map.map_array[0])): # out of bounds
			unit.update_direction(direction)
			return
		elif new_pos[1] < 0 or new_pos[1] >= (len(self.map.map_array)): # out of bounds
			unit.update_direction(direction)
			return

		if self.map.map_array[new_pos[1]][new_pos[0]] == "W": # water
			unit.update_direction(direction)
			return
		# elif self.map_objects[new_pos[1]][new_pos[0]] != ".": # Objects
		elif self.map.map_objects[new_pos[1]][new_pos[0]] != "." and self.map.map_objects[new_pos[1]][new_pos[0]] != "T": # Objects except tall grass
			unit.update_direction(direction)
			return

		for obj in self.objects:
			# print(list(obj.pos), new_pos)
			if list(obj.pos) == new_pos:
				unit.update_direction(direction)
				return
		
		unit.update_pos(new_pos, direction)
		self.find_pokemon(unit, new_pos)

	def find_pokemon(self, player, new_pos):
		# print([player.pos[0], player.pos[1]], " | ", new_pos)
		if [player.pos[0], player.pos[1]] == new_pos:
			if self.map.map_objects[player.pos[1]][player.pos[0]] == "T":
				print("Tall grass")
				if random.randint(0, 100) <= 20:
					print("Pokemon")

	def interact(self):
		if self.player.direction == "up":
			if self.player.pos[1] - 1 < 0: # out of bounds
				print("can't interact (out of bounds)")
				return
			pos = [self.player.pos[0], self.player.pos[1] - 1]
		elif self.player.direction == "down":
			if self.player.pos[1] + 1 >= (len(self.map.map_array[0])): # out of bounds
				print("can't interact (out of bounds)")
				return
			pos = [self.player.pos[0], self.player.pos[1] + 1]
		elif self.player.direction == "left":
			if self.player.pos[0] - 1 < 0: # out of bounds
				print("can't interact (out of bounds)")
				return
			pos = [self.player.pos[0] - 1, self.player.pos[1]]
		elif self.player.direction == "right":
			if self.player.pos[0] + 1 >= (len(self.map.map_array[0])): # out of bounds
				print("can't interact (out of bounds)")
				return
			pos = [self.player.pos[0] + 1, self.player.pos[1]]

		if self.map.map_objects[pos[1]][pos[0]] == "Z":
			print("sign")# TODO: make signs have text
		elif self.map.map_objects[pos[1]][pos[0]] == "P":
			print("item")# TODO: make finding items
		elif self.map.map_objects[pos[1]][pos[0]] == "B":
			print("bush")# TODO: a bush can be cut down if a pokemon in the party has "Cut"
		elif self.map.map_objects[pos[1]][pos[0]] == "R":
			print("rock")# TODO: a rock can be moved down if a pokemon in the party has "Strength" or "Rock Smash"

		print("interact")
