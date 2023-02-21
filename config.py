import os
PATH = os.path.dirname(os.path.abspath(__file__))
print(PATH)

# ─── Colors ───────────────────────────────────────────────────────────────────

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# ─── Screen ───────────────────────────────────────────────────────────────────

SCREEN_SIZE = WIDTH, HEIGHT = 640, 480

SCALE = 80
SCALE = 32 

FONT = {
	"pokemon": os.path.join(PATH, "fonts\\PokemonGb-RAeo.ttf"),
}

# ─── Other Settings ───────────────────────────────────────────────────────────

LOGO = os.path.join(PATH, "img\\sprites\\treebtm.png")

# ─── Map ──────────────────────────────────────────────────────────────────────

MAP = "05"

MAP_FILE = os.path.join(PATH, "maps\\" + MAP + ".txt")
OBJ_FILE = os.path.join(PATH, "maps\\" + MAP + ".obj.txt")

# ─── Sprites ──────────────────────────────────────────────────────────────────

SPRITE_PATH = os.path.join(PATH, "img\\sprites\\")

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
	"air": SPRITE_PATH + "air.png",
	"tallgrass": SPRITE_PATH + "tallgrass.png",
	"grass": SPRITE_PATH + "grass.png",
	"dirt": SPRITE_PATH + "dirt.png",
	"stone": SPRITE_PATH + "stone.png",
	"water": SPRITE_PATH + "water.png",
	"treetop": SPRITE_PATH + "treetop.png",
	"treebtm": SPRITE_PATH + "treebtm.png",
	"treedbl": SPRITE_PATH + "treedbl.png",
	"sign": SPRITE_PATH + "sign.png",
	"item": SPRITE_PATH + "worlditem.png",
	"bush": SPRITE_PATH + "bush.png",
	"rock": SPRITE_PATH + "rock.png",
}

PLAYER_SPRITE = {
	"000down": SPRITE_PATH + "player1.png",
	"000up": SPRITE_PATH + "player1.png", # No sprite for this direction
	"000left": SPRITE_PATH + "player1.png", # No sprite for this direction
	"000right": SPRITE_PATH + "player1.png", # No sprite for this direction
	"001up": SPRITE_PATH + "h001_n.png",
	"001down": SPRITE_PATH + "h001_s.png",
	"001left": SPRITE_PATH + "h001_w.png",
	"001right": SPRITE_PATH + "h001_e.png",
	"002up": SPRITE_PATH + "h002_n.png",
	"002down": SPRITE_PATH + "h002_s.png",
	"002left": SPRITE_PATH + "h002_w.png",
	"002right": SPRITE_PATH + "h002_e.png",
	"003up": SPRITE_PATH + "h003_n.png",
	"003down": SPRITE_PATH + "h003_s.png",
	"003left": SPRITE_PATH + "h003_w.png",
	"003right": SPRITE_PATH + "h003_e.png",
	"004up": SPRITE_PATH + "h004_n.png",
	"004down": SPRITE_PATH + "h004_s.png",
	"004left": SPRITE_PATH + "h004_w.png",
	"004right": SPRITE_PATH + "h004_e.png",
	"005up": SPRITE_PATH + "h005_n.png",
	"005down": SPRITE_PATH + "h005_s.png",
	"005left": SPRITE_PATH + "h005_w.png",
	"005right": SPRITE_PATH + "h005_e.png",
}

POKEMON_IMG_PATH = os.path.join('C:\\Code\\SMX2\\M14\\UF1\\Projecte\\pokemon\\sprites\\PKMNs\\')

POKEMON_SPRITE = {
	"treeko": POKEMON_IMG_PATH + "001_f.png",
	"charmander": POKEMON_IMG_PATH + "004_f.png",
	"totodile": POKEMON_IMG_PATH + "007_f.png",
}

# ─── Images ───────────────────────────────────────────────────────────────────

BG_PATH = os.path.join(PATH, "img\\backgrounds\\")

BG = {
	"start": BG_PATH + "cover.png",
	"start text": BG_PATH + "cover_text.png",
}
