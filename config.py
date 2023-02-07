import os
PATH = os.path.dirname(os.path.abspath(__file__))
print(PATH)

# ─── Colors ───────────────────────────────────────────────────────────────────

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ─── Screen ───────────────────────────────────────────────────────────────────

SCREEN_SIZE = WIDTH, HEIGHT = 640, 480

SCALE = 32

# ─── Other Settings ───────────────────────────────────────────────────────────

LOGO = os.path.join(PATH, "sprites\\treebtm.png")

# ─── Map ──────────────────────────────────────────────────────────────────────

MAP = "05"

MAP_FILE = os.path.join(PATH, "maps\\" + MAP + ".txt")
OBJ_FILE = os.path.join(PATH, "maps\\" + MAP + ".obj.txt")

# ─── Sprites ──────────────────────────────────────────────────────────────────

SPATH = os.path.join(PATH, "sprites\\")

MAP_TILE_NAME = {
	"air": ".",
	"tallgrass": "T",
	"grass": "G",
	"dirt": "D",
	"stone": "S",
	"water": "W",
	"treetop": "N",
	"treebtm": "M",
	"treedbl": "J",
	"sign": "Z",
	"pokeball": "P",
	"bush": "B",
	"rock": "R",
}

TILES = {
	"air": SPATH + "air.png",
	"tallgrass": SPATH + "tallgrass.png",
	"grass": SPATH + "grass.png",
	"dirt": SPATH + "dirt.png",
	"stone": SPATH + "stone.png",
	"water": SPATH + "water.png",
	"treetop": SPATH + "treetop.png",
	"treebtm": SPATH + "treebtm.png",
	"treedbl": SPATH + "treedbl.png",
	"sign": SPATH + "sign.png",
	"pokeball": SPATH + "shroom.png",
	"bush": SPATH + "bush.png",
	"rock": SPATH + "rock.png",
}

PLAYER_SPRITE = {
	"000down": SPATH + "player1.png",
	"000up": SPATH + "player1.png", # No sprite for this direction
	"000left": SPATH + "player1.png", # No sprite for this direction
	"000right": SPATH + "player1.png", # No sprite for this direction
	"001up": SPATH + "h001_n.png",
	"001down": SPATH + "h001_s.png",
	"001left": SPATH + "h001_w.png",
	"001right": SPATH + "h001_e.png",
	"002up": SPATH + "h002_n.png",
	"002down": SPATH + "h002_s.png",
	"002left": SPATH + "h002_w.png",
	"002right": SPATH + "h002_e.png",
	"003up": SPATH + "h003_n.png",
	"003down": SPATH + "h003_s.png",
	"003left": SPATH + "h003_w.png",
	"003right": SPATH + "h003_e.png",
}
