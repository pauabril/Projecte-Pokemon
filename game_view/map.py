import pygame

import config


class Map:
	def __init__(self, screen):
		self.screen = screen
		self.map_array = []
		self.map_objects = []
		self.cam = [0, 0]

	def load(self): # TODO: change maps to csv
		with open(config.MAP_FILE) as map_file:
			for line in map_file:
				map_line = []
				for i in range(0, len(line) - 1, 2):
					map_line.append(line[i])
				self.map_array.append(map_line)

		self.load_objects()

	def load_objects(self): # TODO: change maps to csv
		with open(config.OBJ_FILE) as map_file:
			for line in map_file:
				map_line = []
				for i in range(0, len(line) - 1, 2):
					map_line.append(line[i])
				self.map_objects.append(map_line)


	def render(self, screen, player, objects):
		self.determine_cam(player)

		y_pos = 0
		for line in self.map_array:
			x_pos = 0
			for tile in line:
				img = map_tile_img[tile]
				rect = pygame.Rect(x_pos * config.SCALE - (self.cam[0] * config.SCALE), y_pos * config.SCALE - (self.cam[1] * config.SCALE), config.SCALE, config.SCALE)
				screen.blit(img, rect)

				x_pos += 1
			y_pos += 1

		self.render_objects(screen)

		for obj in objects:
			obj.render(self.screen, self.cam)

	def render_objects(self, screen):
		y_pos = 0
		for line in self.map_objects:
			x_pos = 0
			for tile in line:
				img = map_tile_img[tile]
				rect = pygame.Rect(x_pos * config.SCALE - (self.cam[0] * config.SCALE), y_pos * config.SCALE - (self.cam[1] * config.SCALE), config.SCALE, config.SCALE)
				screen.blit(img, rect)

				x_pos += 1
			y_pos += 1


	def determine_cam(self, player):
		max_y_pos = len(self.map_array) - int(config.SCREEN_SIZE[1] / config.SCALE)
		y_pos = player.pos[1] - int(config.SCREEN_SIZE[1] / config.SCALE / 2)

		if y_pos <= max_y_pos and y_pos >= 0:
			self.cam[1] = y_pos
		elif y_pos < 0:
			self.cam[1] = 0
		else:
			self.cam[1] = max_y_pos

		max_x_pos = len(self.map_array[0]) - int(config.SCREEN_SIZE[0] / config.SCALE)
		x_pos = player.pos[0] - int(config.SCREEN_SIZE[0] / config.SCALE / 2)

		if x_pos <= max_x_pos and x_pos >= 0:
			self.cam[0] = x_pos
		elif x_pos < 0:
			self.cam[0] = 0
		else:
			self.cam[0] = max_x_pos


map_tile_img = {
	"T" : pygame.transform.scale(pygame.image.load(config.TILES["tallgrass"]), (config.SCALE, config.SCALE)),
	"." : pygame.transform.scale(pygame.image.load(config.TILES["air"]), (config.SCALE, config.SCALE)),
	"G" : pygame.transform.scale(pygame.image.load(config.TILES["grass"]), (config.SCALE, config.SCALE)),
	"D" : pygame.transform.scale(pygame.image.load(config.TILES["dirt"]), (config.SCALE, config.SCALE)),
	"S" : pygame.transform.scale(pygame.image.load(config.TILES["stone"]), (config.SCALE, config.SCALE)),
	"W" : pygame.transform.scale(pygame.image.load(config.TILES["water"]), (config.SCALE, config.SCALE)),
	"M" : pygame.transform.scale(pygame.image.load(config.TILES["treebtm"]), (config.SCALE, config.SCALE)),
	"N" : pygame.transform.scale(pygame.image.load(config.TILES["treetop"]), (config.SCALE, config.SCALE)),
	"J" : pygame.transform.scale(pygame.image.load(config.TILES["treedbl"]), (config.SCALE, config.SCALE)),
	"Z" : pygame.transform.scale(pygame.image.load(config.TILES["sign"]), (config.SCALE, config.SCALE)),
	"P" : pygame.transform.scale(pygame.image.load(config.TILES["item"]), (config.SCALE, config.SCALE)),
	"B" : pygame.transform.scale(pygame.image.load(config.TILES["bush"]), (config.SCALE, config.SCALE)),
	"R" : pygame.transform.scale(pygame.image.load(config.TILES["rock"]), (config.SCALE, config.SCALE)),
}
