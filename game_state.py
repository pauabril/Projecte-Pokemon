from enum import Enum

class GlobalGameState(Enum):
	NONE = 0,
	RUNNING = 1,
	PAUSED = 2,
	ENDED = 3,

class RunningGameState(Enum):
	MAP = 0,
	BATTLE = 1
