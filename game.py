import pygame
from player import Player
from npc import Npc
from game_state import GameState
from config import *
import random

import time # NOTE: only for testing start screen

class Game:
	def __init__(self, screen):
		self.screen = screen
		self.objects = []
		self.game_state = GameState.NONE
		self.map = []
		self.map_objects = []
		self.cam = [0, 0]

	def setup(self):
		# self.screen.blit(pygame.image.load(BG["start"]).convert(), (0,0))
		# pygame.display.update()

		player = Player(1,1, snum="001") # TODO: move snum to user input
		self.player = player
		self.objects.append(player)

		self.load_map()

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

		self.game_state = GameState.RUNNING
		print("Setup")

		# time.sleep(1) # REMOVE
					

	def update(self):
		self.screen.fill(BLACK)

		self.handle_events()

		self.render_map(self.screen)

		for obj in self.objects:
			obj.render(self.screen, self.cam)

		# print("Update")

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.game_state = GameState.ENDED

			# ─── Handle Key Events ────────────────────────────────
			elif event.type == pygame.KEYDOWN:
				match event.key:
					case pygame.K_ESCAPE:
						self.game_state = GameState.NONE
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


	def load_map(self): # TODO: change maps to csv
		with open(MAP_FILE) as map_file:
			for line in map_file:
				map_line = []
				for i in range(0, len(line) - 1, 2):
					map_line.append(line[i])
				self.map.append(map_line)

		self.load_map_objects()			

	def render_map(self, screen):
		self.determine_cam()

		y_pos = 0
		for line in self.map:
			x_pos = 0
			for tile in line:
				img = map_tile_img[tile]
				rect = pygame.Rect(x_pos * SCALE - (self.cam[0] * SCALE), y_pos * SCALE - (self.cam[1] * SCALE), SCALE, SCALE)
				screen.blit(img, rect)

				x_pos += 1
			y_pos += 1

		self.render_map_objects(screen)

	def load_map_objects(self): # TODO: change maps to csv
		with open(OBJ_FILE) as map_file:
			for line in map_file:
				map_line = []
				for i in range(0, len(line) - 1, 2):
					map_line.append(line[i])
				self.map_objects.append(map_line)

	def render_map_objects(self, screen):
		y_pos = 0
		for line in self.map_objects:
			x_pos = 0
			for tile in line:
				img = map_tile_img[tile]
				rect = pygame.Rect(x_pos * SCALE - (self.cam[0] * SCALE), y_pos * SCALE - (self.cam[1] * SCALE), SCALE, SCALE)
				screen.blit(img, rect)

				x_pos += 1
			y_pos += 1


	def move_unit(self, unit, pos_change, direction):
		new_pos = [unit.pos[0] + pos_change[0], unit.pos[1] + pos_change[1]]

		if new_pos[0] < 0 or new_pos[0] >= (len(self.map[0])): # out of bounds
			unit.update_direction(direction)
			return
		elif new_pos[1] < 0 or new_pos[1] >= (len(self.map)): # out of bounds
			unit.update_direction(direction)
			return

		if self.map[new_pos[1]][new_pos[0]] == "W": # water
			unit.update_direction(direction)
			return
		# elif self.map_objects[new_pos[1]][new_pos[0]] != ".": # Objects
		elif self.map_objects[new_pos[1]][new_pos[0]] != "." and self.map_objects[new_pos[1]][new_pos[0]] != "T": # Objects except tall grass
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
			if self.map_objects[player.pos[1]][player.pos[0]] == "T":
				print("Tall grass")
				if random.randint(0, 100) <= 20:
					print("Pokemon")


	def determine_cam(self):
		max_y_pos = len(self.map) - int(SCREEN_SIZE[1] / SCALE)
		y_pos = self.player.pos[1] - int(SCREEN_SIZE[1] / SCALE / 2)

		if y_pos <= max_y_pos and y_pos >= 0:
			self.cam[1] = y_pos
		elif y_pos < 0:
			self.cam[1] = 0
		else:
			self.cam[1] = max_y_pos

		max_x_pos = len(self.map[0]) - int(SCREEN_SIZE[0] / SCALE)
		x_pos = self.player.pos[0] - int(SCREEN_SIZE[0] / SCALE / 2)

		if x_pos <= max_x_pos and x_pos >= 0:
			self.cam[0] = x_pos
		elif x_pos < 0:
			self.cam[0] = 0
		else:
			self.cam[0] = max_x_pos


	def interact(self):
		if self.player.direction == "up":
			if self.player.pos[1] - 1 < 0: # out of bounds
				print("can't interact (out of bounds)")
				return
			pos = [self.player.pos[0], self.player.pos[1] - 1]
		elif self.player.direction == "down":
			if self.player.pos[1] + 1 >= (len(self.map[0])): # out of bounds
				print("can't interact (out of bounds)")
				return
			pos = [self.player.pos[0], self.player.pos[1] + 1]
		elif self.player.direction == "left":
			if self.player.pos[0] - 1 < 0: # out of bounds
				print("can't interact (out of bounds)")
				return
			pos = [self.player.pos[0] - 1, self.player.pos[1]]
		elif self.player.direction == "right":
			if self.player.pos[0] + 1 >= (len(self.map[0])): # out of bounds
				print("can't interact (out of bounds)")
				return
			pos = [self.player.pos[0] + 1, self.player.pos[1]]

		if self.map_objects[pos[1]][pos[0]] == "Z":
			print("sign")# TODO: make signs have text
		elif self.map_objects[pos[1]][pos[0]] == "P":
			print("item")# TODO: make finding items
		elif self.map_objects[pos[1]][pos[0]] == "B":
			print("bush")# TODO: a bush can be cut down if a pokemon in the party has "Cut"
		elif self.map_objects[pos[1]][pos[0]] == "R":
			print("rock")# TODO: a rock can be moved down if a pokemon in the party has "Strength" or "Rock Smash"

		print("interact")


map_tile_img = {
	"T" : pygame.transform.scale(pygame.image.load(TILES["tallgrass"]), (SCALE, SCALE)),
	"." : pygame.transform.scale(pygame.image.load(TILES["air"]), (SCALE, SCALE)),
	"G" : pygame.transform.scale(pygame.image.load(TILES["grass"]), (SCALE, SCALE)),
	"D" : pygame.transform.scale(pygame.image.load(TILES["dirt"]), (SCALE, SCALE)),
	"S" : pygame.transform.scale(pygame.image.load(TILES["stone"]), (SCALE, SCALE)),
	"W" : pygame.transform.scale(pygame.image.load(TILES["water"]), (SCALE, SCALE)),
	"M" : pygame.transform.scale(pygame.image.load(TILES["treebtm"]), (SCALE, SCALE)),
	"N" : pygame.transform.scale(pygame.image.load(TILES["treetop"]), (SCALE, SCALE)),
	"J" : pygame.transform.scale(pygame.image.load(TILES["treedbl"]), (SCALE, SCALE)),
	"Z" : pygame.transform.scale(pygame.image.load(TILES["sign"]), (SCALE, SCALE)),
	"P" : pygame.transform.scale(pygame.image.load(TILES["item"]), (SCALE, SCALE)),
	"B" : pygame.transform.scale(pygame.image.load(TILES["bush"]), (SCALE, SCALE)),
	"R" : pygame.transform.scale(pygame.image.load(TILES["rock"]), (SCALE, SCALE)),
}
